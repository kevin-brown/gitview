from django.views.generic import TemplateView
from gitview.repositories import mixins


class SettingsView(mixins.RepositoryMixin, mixins.SettingsSectionMixin,
                   TemplateView):
    template_name = "repositories/settings/index.html"

    def get_context_data(self, **kwargs):
        kwargs["branches"] = self.git_repository.branches

        return super(SettingsView, self).get_context_data(**kwargs)
