# Text_to_Music(Mubert API)

python project for Text to Music with Mubert API

## Requirements

-CUDA GPU<br>
-Anaconda<br>
-python 3.10 above<br>
-pytorch GPU version<br>
-sentence-transformers<br>
-Mubert API<br>
-others: see conda_requirements.txt<br>

# Install

## clone this repo

use git

## create conda enviroment

```conda
$ conda create --name <env> --fileconda_requirements.txt
```

## manual create

conda（python 3.10）

```conda
$ conda create --name <env> python=3.10
```

```conda
$ conda activate <env>
```

pythorch CUDA<br>
see you command form https://pytorch.org/get-started/locally/

```conda
$ conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
```

sentence-transformers

```conda
conda install -c conda-forge sentence-transformers
```

others<br>
flask,httpx

# Run App

go to text_to_music directory and do below<br>
run localhost(127.0.0.1) and port 8080<br>

```bash
python app.py
```

you can port option(-p or -port)

```bash
python app.py -p 8081
```

access http://127.0.0.0:8080(default)

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
