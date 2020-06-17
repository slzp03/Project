import os
import argparse

from pydub import AudioSegment

def sliceWAV():
    for (dirpath, dirnames, filenames) in os.walk("audio/wav"):
        for filename in filenames:
            if not os.path.isdir('audio/sliced/'+filename.split('.')[0]):
                os.mkdir('audio/sliced/'+filename.split('.')[0])
            if filename.endswith('.wav'):
                try:
                    audio = AudioSegment.from_wav(dirpath+'/'+filename)
                    audio = audio[3000:]
                    print(dirpath+'/'+filename,len(audio))
                    print(len(audio)//3000)
                    for index in range(0,len(audio)//3000):
                        audio_to_slice = audio[index*3000:(index+1)*3000]
                        print(len(audio_to_slice))
                        audio_to_slice.export('audio/sliced/'+filename.split('.')[0]+'/'+filename.split('.')[0]+"_"+str(index)+'.'+filename.split('.')[1],format="wav")

                except:
                    print("ERROR:",dirpath+'/'+filename)

                '''
                filepath = dirpath + '/' + filename
                (path, file_extension) = os.path.splitext(filepath)
                file_extension_final = file_extension.replace('.', '')
                try:
                    track = AudioSegment.from_wav(filepath)
                    wav_filename = filename.replace(file_extension_final, 'wav')
                    wav_path = dirpath + '/../wav/' + wav_filename
                    print('CONVERTING: ' + str(filepath))
                    file_handle = track.export(wav_path, format='wav')
                except:
                    print("ERROR CONVERTING " + str(filepath))
                '''

sliceWAV()