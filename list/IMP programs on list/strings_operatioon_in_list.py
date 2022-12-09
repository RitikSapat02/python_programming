li = "geeksforgeeks"
vowel_li = [x for x in li if x in "aeiou"]
print(vowel_li)

l2= ["geeks","ide","courses",'gfg']
l3 = [x for x in l2 if x.startswith("g")]
print(l3)

l4= ["geeks","ide","courses",'gfg']
l5 = [x.upper() for x in l4 if x.startswith("g")]
print(l5)