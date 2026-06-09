from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'people/search.html'
