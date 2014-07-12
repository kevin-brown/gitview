from django.contrib.auth.forms import AuthenticationForm
from gitview.core.forms import Form
from gitview.core import widgets


class AuthenticationForm(AuthenticationForm, Form):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget = widgets.TextInput()
        self.fields["username"].widget.is_required = True

        self.fields["password"].widget = widgets.PasswordInput()
        self.fields["password"].widget.is_required = True
