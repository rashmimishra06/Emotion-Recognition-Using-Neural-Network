from django.shortcuts import render, redirect
import librosa
import soundfile
import os, glob, pickle
import numpy as np

from mysite import settings
from .sustain import model
from .forms import EmoForm
from .models import Inputemo as Input_table
from .deleteObject import delete_info

#delete_info()
for item in Input_table.objects.all():
    print(item.emo_name)

var = False

print('The code is working')

def handler(request):
    if var:
        obj = Input_table.objects.values_list('file', flat=True).order_by('-emo_id')[:1]
        path_to_file = obj[0]
        data = transform_data(path_to_file)
        print(np.array([data]).reshape(1, -1).shape)
        res = model.predict(np.array([data]).reshape(1, -1))
    else:
        res = False

    return render(request, "index.html", {'response': res})


def uploading(request):
    if request.method == 'POST':
        form = EmoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            global var
            var = True
            return redirect('homepage')
    else:
        form = EmoForm()
    return render(request, 'upload.html', {'form': form})


def transform_data(file_path):
    x = []
    file_p = file_path.split('/')[1]
    file = glob.glob(r"polls/my_data/my_data/" + file_p)
    print(file)
    feature = extract_feature(file[0], mfcc=True, chroma=True, mel=True)
    x.append(feature)
    return x


def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        print('this block is working')
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma:
            stft = np.abs(librosa.stft(X))
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
            result = np.hstack((result, chroma))
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
            result = np.hstack((result, mel))
    return result
