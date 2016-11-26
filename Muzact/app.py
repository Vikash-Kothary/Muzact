from flask import Flask
#from app import views

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return 'Hello World'

if __name__=='__main__':
	app.run('0.0.0.0', debug='True')
