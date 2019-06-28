from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from zxcvbn import zxcvbn



class PasswordStrengthValidator:
    def __init__(self, min_strength=3):
        self.min_strength = min_strength

    def validate(self, password, user=None):
        results = zxcvbn(password)
        score = results.get('score', 0)
        if score < self.min_strength:
            raise ValidationError(
                _("This password must have a strength of at least %(min_strength)d."),
                code='password_too_weak',
                params={'min_strength': self.min_strength},
            )

    def get_help_text(self):
        return _(
            "Your password strength must be at least %(min_strength)d."
            % {'min_strength': self.min_strength}
        )
