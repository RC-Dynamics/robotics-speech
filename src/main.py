import speech_recognition as sr



sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
grammar = nltk.data.load('src/athome.cfg')
rd_parser = nltk.RecursiveDescentParser(grammar)
trees = rd_parser.parse(sent)