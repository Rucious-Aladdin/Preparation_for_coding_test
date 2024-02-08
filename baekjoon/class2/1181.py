N = int(input())

words =[]
words_length = []

for i in range(N):
    word = input()
    words.append(word)

words = list(set(words))
    
for x in words:
    words_length.append((x, len(x)))

words_length = sorted(words_length, key = lambda x : (x[1], x[0]))

for w in words_length:
    print(w[0])