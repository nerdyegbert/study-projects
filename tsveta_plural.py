nouns = ['house', 'dog', 'frosty', 'city', 'laptop', 'wolf', 'tree', 'tomato', 'box', 'ray']
i = 0
word = nouns[i]

while i < len(nouns):
    if word.endswith('fe'):
        word[:-2] + 'ves'
    elif word.endswith('f'):
        word[:-1] + 'ves'
    elif word.endswith('o'):
        word + 'es'
    elif word.endswith('us'):
        word[:-2] + 'i'
    elif word.endswith('on'):
        word[:-2] + 'a'
    elif word[-2] not in 'aieou' and word.endswith('y'):
        word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        word + 'es'
    elif word.endswith('an'):
        word[:-2] + 'en'
    else:
        word + 's'

print(word)
i += 1