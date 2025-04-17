"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import Field
from wtforms.fields.numeric import IntegerField
from wtforms.validators import InputRequired


def number_length(min: int, max: int, message: Optional[str] = None):
    def number_length(form, field):
        number_str = str(field.data)
        if field.data < 0 or len(number_str) != 10:
            raise ValidationError("Номер телефона должен содержать ровно 10 цифр "
                                  "и быть положительным")

    phone = IntegerField(validators=[InputRequired(), number_length])


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message or f"Число должно быть от {min} до {max} цифр."

    def __call__(self, form: FlaskForm, field):
        value_str = str(field.data)

        if len(value_str) < self.min or len(value_str) > self.max:
            raise ValidationError(self.message)