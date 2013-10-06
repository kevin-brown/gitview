from django.views.generic import TemplateView


class CodeView(TemplateView):
    template_name = "repositories/code.html"
