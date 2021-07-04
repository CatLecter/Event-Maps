from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user


blueprint = Blueprint("news", __name__, url_prefix="/news")


@blueprint.route("/news")
def news():
    title = "HOME"
    return render_template(
        "news/news.html",
        page_title=title,
    )
