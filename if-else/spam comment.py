text=input("ENter your comment: ")
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True 
elif("subscribe this" in text):
    spam=True
else:
    spam=False 

if(spam):
    print("This comment is spam")
else:
    print("This comment is not spam")