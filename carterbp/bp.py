from flask import Blueprint, render_template, request
from carterbp.squares import Squares

algorithm_bp = Blueprint('carterbp', __name__,
                         template_folder='templates',)


@algorithm_bp.route('/squares', methods=["GET", "POST"])
def square():
    if request.form:
        return render_template("squares.html", fibonacci=Squares(int(request.form.get("series"))))
    return render_template("squares.html", fibonacci=Squares(2))