import requests
import json

def main():
	with open('out.json', 'r') as f:
		questions = json.load(f)

	for question in questions:
		img_data = requests.get(question['image_url']).content

		with open("images/" + question['image_url'].split("/")[-1], 'wb') as handler:
			handler.write(img_data)

if __name__ == '__main__':
	main()