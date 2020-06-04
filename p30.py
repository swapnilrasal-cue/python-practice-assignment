import random

def chooseRandomWord():
    with open('sowpods.txt') as f:
        words = list(f)
    print(random.choice(words).strip())

if __name__ == "__main__":
	chooseRandomWord()