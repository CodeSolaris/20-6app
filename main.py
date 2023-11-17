from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api_v1(station, date):
    pd.read_csv("data.csv")
    return render_template("api_v1.html", station=station, date=date)


if __name__ == "__main__":
    app.run(debug=True)
