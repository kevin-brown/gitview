from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "auth/profile/index.html"

    def get_context_data(self, **kwargs):
        from gitview.auth.models import User
        from gitview.repositories.models import Repository
        from django.http import Http404

        owner_name = self.kwargs["owner_name"]
        
        try:
            owner = User.objects.get_by_natural_key(owner_name)
        except User.DoesNotExist:
            raise Http404("There is no owner here")

        kwargs["profile_owner"] = owner

        owner_repos = Repository.objects.filter_for_user(owner)

        kwargs["profile_repositories"] = owner_repos

        return super(IndexView, self).get_context_data(**kwargs)
