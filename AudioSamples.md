# Finding and converting audio samples

## The basic way

Write a simple Python script to record a short, few seconds, WAV file.

## The automated way

Use a ffmpeg command to convert the first few seconds of an audio file in MP3 or other format to WAV.

e.g. To make 10 second clips in 8000 samples/sec WAV.

```sh
 ffmpeg -t 10 -i in-file.mp3 -acodec pcm_s16le -ac 1 -ar 8000 out-file.wav
```

<https://www.ffmpeg.org/>

You can run ffmpeg in a Docker container or a cloud host - no audio in/out needed as it's just converting files.

## Online converter

There are several of these.  This one seems to work well, and is free.
<https://cloudconvert.com/>

## Finding music and sound effects

I used the 78 rpm archive here

<https://archive.org/details/78rpm>
