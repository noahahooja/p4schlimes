from flask import Blueprint, render_template, request
from ryanbp.minilab import Minilab

minilab_bp = Blueprint('ryan.bp', __name__,
                      template_folder='templates',)


@minilab_bp.route('/minilab', methods=["GET", "POST"])
def minilab():
    if request.form:
        return render_template("minilab.html", minilab=Minilab(int(request.form.get("series"))))
    return render_template("minilab.html", minilab=Minilab(2))
