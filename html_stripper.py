from io import StringIO
from html.parser import HTMLParser
import json

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d): # type: ignore
        self.text.write(d)  # type: ignore
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html: str):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def strip_all_html_from_questions():
    with open('out.json', 'r') as f:
        questions: list[dict[str, str]] = json.load(f)

    for i, question in enumerate(questions) :
        questions[i]['title'] = strip_tags(question['title']).replace("\n", "")
    
    with open('stripped.json', 'w+') as f:
        f.write(json.dumps(questions, indent=4))

def main():
    strip_all_html_from_questions()

if __name__ == '__main__':
    main()