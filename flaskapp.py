from flask import Flask, render_template, redirect
import os
app = Flask(__name__)
ps = [
    "Name: Dương Thế Bách",
    "Work: Student",
    "School: University Of Transport Technology"
]
@app.route("/about-me")
def homepage():
    return render_template("flaskapp.html", posts=ps, title="Giới thiệu")
@app.route("/school")
def school():
    return redirect("http://techkids.vn",code=302)
if __name__ == "__main__":
    app.run(debug=True)
    post = int(os.environ.get("POST", 5000))
    app.run(host="0.0.0.0",post=post) 