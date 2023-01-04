import json

def sort_questions(questions: list[object]):
    return sorted(questions, key=(lambda x: x['title'])) # type: ignore

def remove_duplicates(questions: list[object]):
    return list(set(questions))

def main():
    with open('out.json', 'r') as f:
        questions = json.load(f)
    print(questions)
    questions = remove_duplicates(questions)

    
    with open('sorted.json', 'w+') as f:
        f.write(json.dumps(questions))
    
if __name__ == '__main__':
    main()