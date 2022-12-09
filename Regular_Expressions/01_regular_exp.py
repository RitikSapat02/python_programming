import re

text = "The agent's phone phone phone number is 408-555-1234. call soon!"

# print("number" in text)

pattern = "NOT IN TEXT"
re.search(pattern,text)

pattern = "phone"
match = re.search(pattern,text)
print(match)

print(match.span())
print(match.start())
print(match.end())
