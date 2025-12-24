with open("poems.txt") as f:
    words=f.read()
    if("twinkle" in words):
        print("It contain the word twinkle ")
    else:
        print("It does not contain the word twinkle ")