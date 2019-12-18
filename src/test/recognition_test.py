import os
import json

import speech_recognition as sr

def get_files(audio_path):
    audio_files = []
    audio_names = []

    for file_name in os.listdir(audio_path):
        if file_name.endswith('.wav'):
            audio_files.append(os.path.join(audio_path, file_name))
            audio_names.append(file_name[:-4])

    return audio_files, audio_names

def initialize_predictions(models):
    predictions = { }

    for key in models.keys():
        predictions[key] = []

    predictions['label'] = []

    return predictions

def main():
    r = sr.Recognizer()

    models = {
        'google': r.recognize_google,
        'pocket_sphinx': r.recognize_sphinx
    }

    try:
        with open('src/test/test_checkpoint.in', 'r') as checkpoint:
            i = int(checkpoint.readline())
    except:
        i = 0


    try:
        with open('src/test/predictions.json') as json_file:
            predictions = json.load(json_file)
    except:
        predictions = initialize_predictions(models)
    
    audio_paths, audio_names = get_files('./audio_samples')
    files = list(zip(audio_paths, audio_names))

    while i < len(files):
        audio_path, audio_name = files[i]
        for model_name in models.keys():
            print('%s - %s' %(audio_name, model_name))
            source_file = sr.AudioFile(audio_path)

            with source_file as source:
                audio = r.record(source)

            repeat = True
            while repeat:
                try:
                    recognition = models[model_name](audio)
                    repeat = False
                except Exception as e:
                    print(e)
            
            predictions['label'].append(audio_name)
            predictions[model_name].append(recognition)
        
        i += 1
        with open('src/test/test_checkpoint.in', 'w') as checkpoint:
            checkpoint.write(str(i))

        with open('src/test/predictions.json', 'w+') as outfile:
            json.dump(predictions, outfile)


if __name__ == "__main__":
    main()