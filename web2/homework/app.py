from flask import Flask, render_template, request
import mlab
from register import Register
mlab.connect()
app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        # 1. Get form & extract data
        form = request.form
        f = form["fullname"]
        e = form["email"]
        u = form["username"]
        p = form["password"]
    
        # 2. Add new post
        new_register = Register(fullname=f, email=e , username=u, password=p)
        new_register.save()
        return "OK"


if __name__ == "__main__":
    app.run(debug=True)