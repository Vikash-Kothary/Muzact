from flask import Flask
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return shazam_request()

def shazam_request():
    headers = {'X-Shazam-Api-Key': '03789B8E-A8CE-4229-A880-7FDE4C4FAEFC',
	'Content-Type':'application/octet-stream'}
    payload = open('assets/hack2.wav', 'rb').read()
    url = 'http://beta.amp.shazam.com/partner/recognise'
    
    response = requests.post(url, data=payload, headers=headers)
    res = json.loads(response)
    artist = res['matches'][0]['metadata']['artist']
    return artist 

if __name__ == '__main__':
    app.run('0.0.0.0', debug = 'True')
