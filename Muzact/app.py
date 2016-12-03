from flask import Flask, request
import requests, json

app = Flask(__name__)

@app.route('/shazam', methods=['GET', 'POST'])
@app.route('/')
def index():
    if request.method == 'POST':
	return "{'artist':'Taylor Swift', 'song':'style'}"
#	return shazam_request(request.data)
    return 'Hello World'

def shazam_request(file):
    headers = {'X-Shazam-Api-Key': '03789B8E-A8CE-4229-A880-7FDE4C4FAEFC',
	'Content-Type':'application/octet-stream'}
    payload = open(file, 'rb').read()
    url = 'http://beta.amp.shazam.com/partner/recognise'
    
    response = requests.post(url, data=payload, headers=headers)
    res = json.loads(response)
    metadata = res['matches'][0]['metadata']
    return metadata 

if __name__ == '__main__':
    app.run('0.0.0.0', debug = 'True')
