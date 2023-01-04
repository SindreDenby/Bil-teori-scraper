import json

def sort_questions(questions: list[dict[str, str]]):
    return sorted(questions, key=(lambda x: x['title'])) # type: ignore

def remove_duplicates(questions: list[dict[str, str]]):
    res_list: list[dict[str, str]] = []
    for i in range(len(questions)):
        if questions[i] not in questions[i + 1:]:
            res_list.append(questions[i])

    return res_list

def remove_duplicates_and_sort(questions: list[dict[str, str]]):
    newQuest = remove_duplicates(questions)
    newQuest = sort_questions(newQuest)

    return newQuest

def main():
    with open('out.json', 'r') as f:
        questions: list[dict[str, str]] = json.load(f)

    questions = remove_duplicates(questions)

    questions = sort_questions(questions)
    with open('cleaned.json', 'w+') as f:
        f.write(json.dumps(questions))
    
if __name__ == '__main__':
    main()