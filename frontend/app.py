import app from flask

print(backend)

@app.route("/")
def home():
	return "home"
