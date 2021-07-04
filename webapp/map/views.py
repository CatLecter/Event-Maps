from flask import Blueprint, render_template

blueprint = Blueprint("map", __name__)


@blueprint.route("/")
def index():
    title = "HOME"
    return render_template(
        "map/ymaps.html",
        page_title=title,
    )
