# 1. Create a flask app
from flask import Flask, render_template

app = Flask(__name__)
ps = [
        "Trong dam gi dep bang sen",
        "La xanh bong trang lai chen nhi vang",
        "Nhi vang bong trang la xanh"
    ]
# 2. Create router
@app.route("/post/<int:a>")
def new_post(a):
    
    return render_template("post_detail.html", post = ps[a], title = "Bach")
@app.route("/")
def homepage():
    
    return render_template("homepage.html", posts = ps, title ="bach")

@app.route("/bach")
def new_homepage():
    return "Hello bach"
@app.route("/hello/<name>")
def hello(name):
    return name
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    result = a + b    
    return str(result)

@app.route("/h1tag")
def h1tag():
    return "<h1>heading 1 - bigggg</h1></p>hom nay toi buon</p>"
# 3. Run app
print("Running app")
if __name__ == "__main__":
    app.run(debug=True) #listening