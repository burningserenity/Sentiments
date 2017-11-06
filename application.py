from flask import Flask, redirect, render_template, request, url_for
import os
import sys
import helpers
from analyzer import Analyzer
positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")
analyzer = Analyzer(positives, negatives)

app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))

app.run(host='0.0.0.0', port=port)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    positive, negative, neutral = 0.0, 0.0, 100.0
    for i in range(len(tweets)):
        tally = analyzer.analyze(tweets[i])
        if tally > 0.0:
            positive = positive + 1.0
            neutral = neutral - 1.0
        elif tally < 0.0:
            negative = negative + 1.0
            neutral = neutral - 1.0

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
