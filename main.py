import app as app
from flask import Flask, render_template
from code_pre_spring_break.carterbp.bp import square_bp

app = Flask(__name__)

app.register_blueprint(square_bp, url_prefix='/code_pre_spring_break/carterbp')



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

@app.route('/noahminilab')
def noahml():
    return render_template("noahminilab.html")

@app.route('/bubblelab')
def carterml():
    return render_template("Bubble.html")

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')

