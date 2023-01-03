import requests
import json
import os.path

def main():
	with open('out.json', 'r') as f:
		questions = json.load(f)

	for i, question in enumerate(questions):
		img_data = requests.get(question['image_url']).content

		# img_name = "images/" + "-".join(question['image_url'].split("/")[5:]) 

		img_name: str = "images/" + question['image_url'].split("/")[-1]

		while os.path.exists(img_name):
			print(img_name, "exists")
			file_type = img_name.split(".")[1]
			img_name = img_name.split(".")[0] + "(1)." + file_type

		with open(img_name, 'wb') as handler:
			handler.write(img_data)

		questions[i]['image_lcoal_path']

		with open('out.json', 'w+') as f:
			f.write(json.dumps(questions, indent=2))

if __name__ == '__main__':
	main()