from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkboard_1():
    return render_template("home.html", color_1 = "black", color_2 = "red", row = 8, col = 8)

@app.route("/<int:num>")
def checkboard_2(num):
    return render_template("home.html", color_1 = "black", color_2 = "red", row = num, col = 8)

if __name__ == "__main__":
    app.run(debug=True)