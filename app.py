import time
import httpx
import json

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from sentence_transformers import SentenceTransformer

from utils import get_tags_for_prompts, get_mubert_tags_embeddings, get_pat

minilm = SentenceTransformer('all-MiniLM-L6-v2')
mubert_tags_embeddings = get_mubert_tags_embeddings(minilm)

app = Flask(__name__, template_folder='./templates')


def get_track_by_tags(tags, pat, duration, maxit=20, loop=False):
    if loop:
        mode = "loop"
    else:
        mode = "track"
    r = httpx.post('https://api-b2b.mubert.com/v2/RecordTrackTTM',
                   json={
                       "method": "RecordTrackTTM",
                       "params": {
                           "pat": pat,
                           "duration": duration,
                           "tags": tags,
                           "mode": mode
                       }
                   })

    rdata = json.loads(r.text)
    assert rdata['status'] == 1, rdata['error']['text']
    trackurl = rdata['data']['tasks'][0]['download_link']

    print('Generating track ', end='')
    for i in range(maxit):
        r = httpx.get(trackurl)
        if r.status_code == 200:
            return trackurl
        time.sleep(1)


def generate_track_by_prompt(email, prompt, duration, loop=False):
    try:
        pat = get_pat(email)
        _, tags = get_tags_for_prompts(
            minilm, mubert_tags_embeddings, [prompt, ])[0]
        return get_track_by_tags(tags, pat, int(duration), loop=loop), "Success", ",".join(tags)
    except Exception as e:
        return None, str(e), ""


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/audio', methods=['POST'])
def generate_audio():
    request_json = request.json
    required = (
        'email',
        'prompt',
        'duration',
        'loop')
    if not all(k in request_json for k in required):
        return 'missing values', 400

    email = request_json['email']
    prompt = request_json['prompt']
    duration = request_json['duration']
    loop = request_json['loop']

    response = generate_track_by_prompt(
        email=email, prompt=prompt,                                        duration=duration,
        loop=loop)

    if not response:
        return 'generate failed', 400

    response_json = {
        'trackurl': response[0],
        'result_message': response[1],
        'tags': response[2]
    }

    return jsonify(response_json), 200


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080,
                        type=int, help='port to listen on')

    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
