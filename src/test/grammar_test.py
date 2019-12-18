import nltk

def create_command(tree):
    command = {}
    command['action'] = tree[0].label()
    command['entity'] = {}
    if tree[1][0].label() == 'PERSON':
        command['entity']['type'] = tree[1][0][0]
    else:
        for word in t[1][0]:
            if word.label() == 'COLOR':
                command['entity']['color'] = word[0]
            if word.label() == 'OBJECT' or word.label() == 'FURNITURE':
                command['entity']['type'] = word[0]
    return command

grammar = nltk.data.load('./grammar/athome.cfg')
rd_parser = nltk.RecursiveDescentParser(grammar)
said = []
said.append('pick up the blue cup')
said.append('navigate to John')
said.append('look at the shelf')

for s in said:
    tokens = nltk.word_tokenize(s)
    trees = rd_parser.parse(tokens)
    for t in trees:
        print(t)
    command = create_command(t)
    print (command)