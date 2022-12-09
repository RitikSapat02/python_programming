from collections import Counter

# mylist = [1,1,1,1,2,3,3,3,3,2,2,2,2,'a','b','a']
# print(Counter(mylist))


# print(Counter("aaabbbbbssss"))

# print(Counter("How many times does each word show up in this sentence with a word"))

# sentence = "How many times does each word show up in this sentence with a word"
# print(Counter(sentence.lower().split()))


letters = "aaaaabbbbbccccdddddd"
c = Counter(letters)
print(c)
# print(c.most_common())
# print(c.most_common()[::-1])


#sum(c.values()) = total of all counts
# print(sum(c.values()))

#c.values
# print(c.values())

#c.clear()
# c.clear()
# print(c)

# print(list(c))
# print(set(c))
# print(dict(c))
# print(c.items())
# print(Counter(dict(c.items())))
# c+=Counter()
# print(c)
# print(c.most_common( )[:-2-1:-1])