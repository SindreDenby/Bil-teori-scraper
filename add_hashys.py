import json
import random


def main():
    with open('stripped.json', 'r') as f:
        questions = json.load(f)

    for i in range(len(questions)):
        questions[i]['id'] = random.getrandbits(128)
    
    with open('hashed.json', 'w+') as f:
        f.write(json.dumps(questions, indent=4))

if __name__ == '__main__':
    main()