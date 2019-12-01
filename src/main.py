import speech_recognition as sr
import nltk
nltk.download('punkt')

grammar = nltk.data.load('./grammar/athome.cfg')
sent = 'pick up the blue cup'
sent = nltk.word_tokenize(sent)
rd_parser = nltk.RecursiveDescentParser(grammar)
trees = rd_parser.parse(sent)
for t in trees:
    print(t)