from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkerboard_1():
    return render_template("home.html", color_1 = "black", color_2 = "red", row = 8, col = 8)

@app.route("/<int:num>")
def checkerboard_2(num):
    return render_template("home.html", color_1 = "black", color_2 = "red", row = num, col = 8)

@app.route("/<int:x>/<int:y>")
def checkerboard_3(x,y):
    return render_template("home.html", color_1 = "black", color_2 = "red", row = x, col = y)

@app.route("/<string:color1>/<int:x>/<string:color2>/<int:y>")
def checkerboard_4(color1,x,color2,y):
    return render_template("home.html", color_1=color1, row=x, color_2=color2, col=y)

if __name__ == "__main__":
    app.run(debug=True)