from flask import Flask, render_template

app = Flask(__name__)

# This is a "route" - it maps a URL to a function
@app.route("/")
def home():
    return render_template("index.html", name="Jazzy")

@app.route("/about")
def about():
    return render_template("index.html", name="About Page")

if __name__ == "__main__":
    app.run(debug=True)