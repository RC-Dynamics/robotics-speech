import speech_recognition as sr
import nltk

grammar = nltk.data.load('./grammar/athome.cfg')

def create_command(tree):
    command = {}
    command['action'] = tree[0][0].label()
    command['entity'] = {}
    if tree[1][1].label() == 'C':
        command['entity']['color'] = tree[1][1][0]
        command['entity']['type'] = tree[1][2][0][0]
    else:
        command['entity']['type'] = tree[1][1][0][0]
    return command

def callback(recognizer, audio):
    global grammar
    rd_parser = nltk.RecursiveDescentParser(grammar)
    try:
        said = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + said)
        tokens = nltk.word_tokenize(said)
        try:
            trees = rd_parser.parse(tokens)
            for t in trees:
                print(t)
            command = create_command(t)
            print (command)
        except ValueError as e:
            print(e)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    r = sr.Recognizer()
    m = sr.Microphone()
    print('Ambient noise check.')
    with m as source:
        r.adjust_for_ambient_noise(source)
    print('Done.')

    stop_listening = r.listen_in_background(m, callback)

    input("Press Enter to stop...\n\n")
    stop_listening(wait_for_stop=False)

if __name__ == "__main__":
    main()