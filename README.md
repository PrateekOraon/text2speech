### Create 'Text to Speech' App using Django, HTML and AWS Polly
![screenshot 4](https://user-images.githubusercontent.com/20254425/39020649-468623a0-444b-11e8-89a5-e7b3ea70b945.png)


1) Install googletrans:

> `pip install googletrans` 

2) Install boto3

> `pip install boto3`

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
