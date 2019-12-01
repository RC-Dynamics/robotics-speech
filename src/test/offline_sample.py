import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('audio_files/harvard.wav')
with harvard as source_h:
    audio_harvard = r.record(source_h)

print ('\nHarvard:')
print ('\tGoogle: ' + r.recognize_google(audio_harvard))
print ('\tPocketSphinx: ' + r.recognize_sphinx(audio_harvard))

r = sr.Recognizer()
jackhammer = sr.AudioFile('audio_files/jackhammer.wav')
with jackhammer as source_j_r:
    audio_jackhammer = r.record(source_j_r)

print ('\nJack Hammer (raw):')
print ('\tGoogle: ' + r.recognize_google(audio_jackhammer))
print ('\tPocketSphinx: ' + r.recognize_sphinx(audio_jackhammer))

r = sr.Recognizer()
jackhammer = sr.AudioFile('audio_files/jackhammer.wav')
with jackhammer as source_j_f:
    r.adjust_for_ambient_noise(source_j_f, duration=0.5)
    audio_jackhammer = r.record(source_j_f)

print ('\nJack Hammer (filter):')
print ('\tGoogle: ' + r.recognize_google(audio_jackhammer))
print ('\tPocketSphinx: ' + r.recognize_sphinx(audio_jackhammer))