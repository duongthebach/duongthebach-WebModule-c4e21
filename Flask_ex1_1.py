from flask import Flask, render_template

app = Flask(__name__)

@app.route("/BMI/<int:w>/<int:h>")
def BMI(w, h):
    BMI = w / (h **2 /10000)
    if BMI < 16:
        r="Severely underweight"
    elif BMI <= 18.5:
        r="Underweight"
    elif BMI <= 25:
        r="Norma"
    elif BMI <=30:
        r="Overweight"
    else:
        r="Obese"
    return render_template("bmi.html", result=r)
if __name__ == "__main__":
    app.run(debug=True)
