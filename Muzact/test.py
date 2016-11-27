from app import app

@app.route('/test')
def testing():
	return 'bants'
