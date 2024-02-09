from webbrowser import open
from math import pi, sqrt
import os

from flask import Flask, render_template, request
from forms import FormulaForm, ResultForm


G = 9.81  # Ускорение свободного падения
C_2 = 0.96  # эмпирический коэффициент
C_1 = 1.3  # эмпирический коэффициент

app = Flask(__name__)


def render(**kw):
    return render_template("index.html", title="Физический калькулятор", **kw)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    form = FormulaForm(request.form)

    if request.method == "POST" and form.validate():
        t = form.t.data
        p_v = form.p_v.data
        p_n = form.p_n.data
        Q_0 = form.Q_0.data
        v = form.v.data

        delta = p_v - p_n / p_v

        A_2 = C_2 * pi * sqrt(t) * (delta * G * Q_0**2 / v)**(1/3)
        R_1 = sqrt(C_1 * t * sqrt(delta * G * Q_0))

        res_form = ResultForm(data={"A_2": A_2, "R_1": R_1})

        return render(form=form, res_form=res_form)
    return render(form=form)


@app.route("/close", methods=["POST"])
def close_app():
    eval("os._exit(0)")


if __name__ == '__main__':
    open("http://localhost:5000")
    app.run(host="localhost")
