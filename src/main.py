import speech_recognition as sr
import nltk
import pyttsx3

grammar = nltk.data.load('./grammar/athome.cfg')
engine = pyttsx3.init()

def create_command(tree):
    command = {}
    command['action'] = tree[0].label()
    command['entity'] = {}
    if tree[1][0].label() == 'PERSON':
        command['entity']['type'] = tree[1][0][0]
    else:
        for word in tree[1][0]:
            if word.label() == 'COLOR':
                command['entity']['color'] = word[0]
            if word.label() == 'OBJECT' or word.label() == 'FURNITURE':
                command['entity']['type'] = word[0]
    return command

def callback(recognizer, audio):
    global grammar
    global engine
    rd_parser = nltk.RecursiveDescentParser(grammar)
    try:
        said = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + said)
        tokens = nltk.word_tokenize(said)
        try:
            trees = rd_parser.parse(tokens)
            for t in trees:
                print(t)
            try:
                command = create_command(t)
                print (command)
                engine.say(command['action'] 
                            + (' ' + command['entity']['color'] if 'color' in command['entity'] else '') 
                            + ' ' + command['entity']['type'])

                engine.runAndWait()
            except:
                engine.say('Sorry, this is not a valid command')
                engine.runAndWait()
                print('Malformed phrase.')

        except ValueError as e:
            print(e)
    except sr.UnknownValueError:
        engine.say('Sorry, I cannot understand what you said, could you repeat please?')
        engine.runAndWait()
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        engine.say('Sorry, I cannot understand what you said, could you repeat please?')
        engine.runAndWait()
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    r = sr.Recognizer()
    m = sr.Microphone()
    print('Ambient noise check.')
    with m as source:
        r.adjust_for_ambient_noise(source)
    print('Done.')

    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=5)

    input("Press Enter to stop...\n\n")
    stop_listening(wait_for_stop=False)
    engine.stop()

if __name__ == "__main__":
    main()