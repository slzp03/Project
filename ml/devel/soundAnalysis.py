import os
from numba import jit
import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from librosa.core.constantq import cqt,stft
from sklearn.model_selection import train_test_split
categories = ['나무데크','모래','아스팔트','자갈','잔디']
audio_path = './audio/sliced/'
num_classes = len(categories)
X = []
Y=[]
for idx, category in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idx] = 1
    audio_dir = audio_path + category + '/'
    for (dirpath,dirnames,filenames) in os.walk(audio_dir):
        for filename in filenames:
            print(audio_dir+filename)
            y, sr = librosa.load(dirpath + '/' + filename)
            cqt_result = cqt(y, sr)
            print(cqt_result.shape)
            print(cqt_result.size)
            X.append(cqt_result)
            Y.append(label)
X = np.array(X)
Y = np.array(Y)
X_train, X_test,Y_Train,Y_Test = train_test_split(X,Y)
xy = (X_train, X_test, Y_Train, Y_Test)

np.save("./sound_data.npy", xy)


'''
for (dirpath, dirnames, filenames) in os.walk("audio/sliced"):
    for filename in filenames:
        print(dirpath+'/'+filename)
        y, sr = librosa.load(dirpath + '/' + filename)
        cqt_result = cqt(y,sr)

        plt.plot()
        plt.show()

        C = np.abs(librosa.cqt(y, sr=sr))
        print(C)
        librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),sr=sr,x_axis='time',y_axis='cqt_note')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Constant-Q power spectrum')
        plt.tight_layout()
        plt.show()

'''