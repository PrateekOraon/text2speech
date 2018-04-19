### Create 'Text to Speech' App using Python, HTML and AWS Polly
![screenshot 2](https://user-images.githubusercontent.com/20254425/38979666-6f54a04a-43d8-11e8-942e-a5ebf225d0f5.png)


1) Install googletrans:

> `<pip install googletrans>` 

2) Install boto3

> `<pip install boto3>`

Make changes to views.py:
```python
response = client.synthesize_speech(
        OutputFormat ='json'|'mp3'|'ogg_vorbis'|'pcm',
        Text=message,
        TextType='ssml'|'text',
        VoiceId='Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|
        'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'
    )
```
