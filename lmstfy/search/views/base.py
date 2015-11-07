from django.views.generic import TemplateView


class SearchBaseView(TemplateView):
    template_name = "base.html"
