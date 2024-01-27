from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", color_1 = "black", color_2 = "red", num = 8)

if __name__ == "__main__":
    app.run(debug=True)