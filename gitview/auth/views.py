from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import resolve_url
from django.views.generic import FormView, RedirectView

from gitview.auth.forms import AuthenticationForm


class LoginView(FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = "auth/login.html"

    def form_valid(self, form):
        from django.contrib.auth import login

        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        from django.conf import settings
        import urlparse

        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.request.REQUEST.get(self.redirect_field_name,
                                                   '')

        netloc = urlparse.urlparse(redirect_to)[1]

        if not redirect_to:
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL

        return redirect_to


class LogoutView(RedirectView):
    url = reverse_lazy("index")
    permanent = False

    def get(self, *args, **kwargs):
        from django.contrib.auth import logout

        logout(self.request)

        return super(LogoutView, self).get(*args, **kwargs)
