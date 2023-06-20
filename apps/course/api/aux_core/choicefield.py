from rest_framework.fields import ChoiceField
from django.utils.translation import gettext_lazy as _
from apps.accounts.choices import IDENTIFICATION_CHOICES
from apps.course.choices import GENDER_CHOICES


class ChoiceTypeField(ChoiceField):
    valid_choices = [choice[0] for choice in IDENTIFICATION_CHOICES]
    default_error_messages = {
        'invalid_choice': _(f'The input is not a valid choice. The correct choices are: {valid_choices}')
    }


class ChoiceGenderField(ChoiceField):
    valid_choices = [choice[0] for choice in GENDER_CHOICES]
    default_error_messages = {
        'invalid_choice': _(f'The input is not a valid choice. The correct choices are: {valid_choices}')
    }
