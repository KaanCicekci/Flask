from flask import Flask, render_template
import random

app = Flask(__name__)
names = ["mahmut","elif","eymen","kaan"]
@app.route("/")
def home():
    name = random.choice(names)
    return render_template("index.html",name=name)

if __name__ == '__main__':
    app.run(debug=True)
