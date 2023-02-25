import spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp("cat apple monkey banana skin")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#understandably the most similar is each token compared with themselves at '1.0' similarity score.
#Most similar are cat/monkey and apple/banana pairs as they are same semantic groups, animals and fruit respectively.
#The most disimilar are cat/banana, cat/apple & monkey/apple pairs as neither animal are known to eat these fruits.
#But there is still higher similarity between monkey/banana compared to these pairs as monkeys do eat bananas.
#I added in skin as a test to see if the program recognised that all tokens have skin but similarity scores weren't high
#With monkey being really low at less than 0.1
#The program is able to detect semantic similarities pretty well but still could be better.

print("")

tokens = nlp("cat leopard panther lion tiger")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#I did the above as my own example as per task.
#I was surprised by the 100% similarity score between leopard and tiger and the lack of similarity between panther and every other token!
#They are all types of feline/cat so I would have expected panther to have high similarity.
#and although leopards and tigers are very similar, to have 100% similarity was quite extreme, as one has spots and one has stripes.

print("")

nlp = spacy.load('en_core_web_sm')

tokens = nlp("cat apple monkey banana skin")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#using sm doesn't give us semantic data to compare. It instead compares just tags, parse and entity recognition.