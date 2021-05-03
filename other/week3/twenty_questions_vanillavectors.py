import json

def is_answer(node):
    return len(node) == 1


f = open('../data/questions.json')   # fix path
content = f.read()   # add round brackets
node = json.loads(content)  # loads instead of reads

finished = False

while not finished:   # colon -> syntax error
    print(node['text'])   # added )
    if is_answer(node):   # change name of the function
        finished = True
    else:
        answer = input()    # one equal-sing 
        if answer.lower() in ['yes', 'y']:    # lower instead of upper 
            node = node['yes']   # switch yes and no
        else:
            node = node['no']     # indented whole block 
