from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChoiceAllForm(FlaskForm):
    submit = SubmitField("Все", render_kw={"class": "btn btn-primary fw-bolder"})


class ChoiceRecommendedForm(FlaskForm):
    submit = SubmitField(
        "Рекомендуемые", render_kw={"class": "btn btn-secondary fw-bolder"}
    )


class ChoiceCreatedForm(FlaskForm):
    submit = SubmitField("Созданные", render_kw={"class": "btn btn-info fw-bolder"})
