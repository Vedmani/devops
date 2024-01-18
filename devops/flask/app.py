from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  message = "Hello from Flask on port 6500!"
  return render_template("index.html", message=message)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=6500)
