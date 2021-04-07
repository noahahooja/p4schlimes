from flask import Blueprint, render_template, request
from carterbp.squares import Squares

square_bp = Blueprint('squarebp', __name__,
                      template_folder='templates',)


@square_bp.route('/squares', methods=["GET", "POST"])
def square():
    if request.form:
        return render_template("squares.html", squares=Squares(int(request.form.get("series"))))
    return render_template("squares.html", squares=Squares(2))