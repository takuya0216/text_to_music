# Text_to_Music(Mubert API)

python project for Text to Music with Mubert API

## Requirements

-Anaconda<br>
-python 3.10 above<br>
-pytorch version<br>
-sentence-transformers<br>
-Mubert API<br>
-others: see conda_requirements.txt<br>

# Install

## clone this repo

use git

## create conda enviroment

maybe an error occurs

```conda
$ conda create --name <env> --file conda_requirements.txt
```

## manual create
step by step insatll.

conda（python 3.10）

```conda
$ conda create --name <env> python=3.10
```

```conda
$ conda activate <env>
```

pythorch<br>
see your command form https://pytorch.org/get-started/locally/

```conda
$ conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
```

sentence-transformers
command from https://www.sbert.net/docs/installation.html

```conda
conda install -c conda-forge sentence-transformers
```

others<br>
flask,httpx

# Run App

go to text_to_music directory and do below<br>

```bash
python app.py
```

you can use port option(-p or -port)
default setting is port 8080<br>

```bash
python app.py -p 8081
```

access http://127.0.0.0:8080(default) or http:your_localip:8080

# Generate Music

fill in input forms. then click send.

## Inputs

### email:

your email. email address is required to use Mubert API. <br>
don't need to Sing up Mubert.com currentry.

### prompt:

text input for your music<br>

### duration

music duration

### loop

loop or track

## Outputs

### Audio

audio out

### Result Message

Succes or Fail
