# django-pass-strength-validator

`django-pass-strength-validator` is a password strength validator for Django based on the [`zxcvbn`](https://github.com/dropbox/zxcvbn) library developed by Dropbox. Any time a user attempts to set a password with a strength less than the specified level, a ValidationError will be raised. This enhances the security of your app by ensuring users have strong passwords.

Through pattern matching and estimation, the zxcvbn library recognizes and weighs 30k common passwords, common names and surnames according to US census data, popular English words from Wikipedia and US television and movies, and other common patterns like dates, repeats (`aaa`), sequences (`abcd`), keyboard patterns (`qwertyuiop`), and l33t speak.

## Installation

```shell
pip install django-pass-strength-validator
```

## Usage in Django

Add a string reference to the PasswordStrengthValidator class from the `django-pass-strength-validator` library in the `AUTH_PASSWORD_VALIDATORS` list in your Django project settings.

The `zxcvbn` library returns a password strength score from 0 to 4, with 0 being the weakest and 4 being the strongest password strength. The default minimum password strength level for the `django-pass-strength-validator` library is 3. This means if a user attempts to save a password that has a strength less than 3, a ValidationError will be raised. You can change the minimum password strength level by passing though an OPTIONS value in Django settings, as shown in the example below.

```python
AUTH_PASSWORD_VALIDATORS = [
    # There will likely be other validators included by default
    {
        'NAME': 'django_pass_strength_validator.PasswordStrengthValidator',
        'OPTIONS': {
            'min_strength': 3, # Optional, can be an integer from 0 to 4
        }
    },
]
```
