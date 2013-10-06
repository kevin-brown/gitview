from django.contrib.auth.forms import AuthenticationForm
from gitview.core.forms import Form


class AuthenticationForm(AuthenticationForm, Form):
    pass
