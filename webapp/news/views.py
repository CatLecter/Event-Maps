from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user


blueprint = Blueprint("news", __name__, url_prefix="/news")


@blueprint.route("/news")
def news():
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    title = "HOME"
    return render_template(
        "news/news.html",
        page_title=title,
    )
