from django.views.generic import FormView
from gitview.auth.forms import AuthenticationForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "auth/login.html"
