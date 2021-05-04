from flask import Flask, render_template, request
from Bubble_Sort.Brayden_Bubble_Sort.braydenbs import BraydenBubbleSort1

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/reactiontest')
def reactiontest():
    return render_template("reactiontest.html")

@app.route('/magic')
def magic():
    return render_template("magic.html")

@app.route('/bio')
def aboutus():
    return render_template("aboutus.html")

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

@app.route('/livechat')
def livechat():
    return render_template("livechat.html")

@app.route('/square')
def squa():
    return render_template("squares.html")

@app.route('/noahminilab')
def noahml():
    return render_template("noahminilab.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/braydenbubsort', methods=["GET", "POST"])
def braydenbubblesort():
    if request.form:
        all_list = []

        all_list.append(int(request.form.get('number1')))
        all_list.append(int(request.form.get('number2')))
        all_list.append(int(request.form.get('number3')))
        return render_template("braydenbubsort.html", testing=BraydenBubbleSort1(all_list))  

    return render_template("braydenbubsort.html")  
      


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')

