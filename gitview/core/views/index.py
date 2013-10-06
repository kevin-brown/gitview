from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "index/dashboard.html"

    def get(self, *args, **kwargs):
        """
        Show the login view if the user is not logged in.
        """

        from gitview.auth.views import LoginView

        if not self.request.user.is_active:
            login_view = LoginView.as_view()
            login_view = login_view(self.request, *args, **kwargs)

            return login_view

        return super(DashboardView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        from gitview.repositories.models import Repository

        kwargs["user_repositories"] = Repository.objects.filter_for_user(
            self.request.user)

        return super(DashboardView, self).get_context_data(**kwargs)
