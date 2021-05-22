"""
Controller file for the web application.

The central file of the application. 
"""

from flask import Flask
from flask import render_template
from flask import request
from simple_recommender import get_recommendations

app = Flask(__name__)


# @app.route("/")  # this is a decorator; The @ signals that it is a decorator
# def hello_world():
#     return "Hello, World!"

# A decorator is a function that takes another function as input argument, adds functionality to the input function and returns it as a function again


@app.route("/")
def index():
    return render_template("index.html", title="Hello Vanilla Vectors!")


@app.route("/recommender")
def recommender():
    html_form_data = dict(request.args)

    recs = get_recommendations()

    print(html_form_data)

    return render_template("recommendations.html", movies=recs)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
