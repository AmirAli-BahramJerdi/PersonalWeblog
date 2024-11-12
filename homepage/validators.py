import re
from django.core.exceptions import ValidationError

def iranian_phone_number_validator(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError("شماره تلفن باید با 09 شروع شده و شامل 11 رقم باشد.")