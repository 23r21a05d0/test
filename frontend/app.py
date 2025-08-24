import app from flask

@app.route("/")
def home():
	return "home"
