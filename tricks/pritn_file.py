import time

while(True):
    with open("Programs/tricks/vegetables.txt") as file:
        print(file.read())
        time.sleep(5)