import random

name = input("Enter your name: ")
sentence = "*proper fell on the *adj *noun today."
sentence = sentence.split()
nouns = ['table', 'chair', 'floor', 'ground', 'staircase', 'playground']
adj = ['huge', 'small', 'tiny', 'enormous', 'humungous']
count = 0;
for word in sentence:
    if (word == '*noun'):
        sentence[count] = random.choice(nouns)
    if (word == '*proper'):
        sentence[count] = name
    if (word == '*adj'):
        sentence[count] = random.choice(adj)
    count += 1

st = ''
for word in sentence:
    st += word + ' '
print(st)


