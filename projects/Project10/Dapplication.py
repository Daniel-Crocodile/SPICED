from flask import Flask
from flask import render_template
from flask import request
from Drecomender import new_user, model_rec, user_rec


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Movie Recommender')

@app.route('/recommender')
def recommender():
    html_form_data = dict(request.args)
    print(html_form_data)

    df = new_user('./../ml-25m/ratings.csv', './../ml-25m/movies.csv', 10_000)
    recs= user_rec(html_form_data, model_rec(df.iloc[0:500_000]))

    return render_template('recommendations.html',
                            movies = recs)

if __name__ == "__main__": 
    app.run(debug=True, port=5000) 