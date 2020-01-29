import requests, json

from flask import Flask, request, redirect, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('homes.html')

@app.route('/historya')
def history():
	table=databases.get_all()
	return render_template('history.html',tt=table)

@app.route('/search', methods = ['POST','GET'])
def search():
	if request.method == 'POST':
		concepts = iden(request.form['url'])
		name=concepts[0]["name"]
		value=concepts[0]["value"]
		return render_template('history.html', name = name,value=value)
	else:
		return render_template('homes.html')


from databases import *
def iden(url):
	headers = {'Authorization': 'Key 4604af50f10d44be90c409f373f75eb3'}

	# this is the url of where your request will go
	api_url = "https://api.clarifai.com/v2/models/e466caa0619f444ab97497640cefc4dc/outputs"

	# this is content of the message(data) you are sending to clarifai
	data ={"inputs": [
	      {
	        "data": {
	          "image": {
	            "url": url
	          }
	        }
	      }
	    ]}

	# putting everything together; sending the request!
	response = requests.post(api_url, headers=headers, data=json.dumps(data))
	response_dict = json.loads(response.content)
	concepts = response_dict["outputs"][0]["data"]["regions"][0]["data"]["face"]["identity"]["concepts"]
	# for concept in concepts:
	best_match = concepts[0]
	print(best_match)
	print(best_match["name"] , best_match["value"])
	add_celeb(best_match["name"], best_match["value"])

	return concepts



if __name__ == '__main__':
    app.run(debug=True)




































