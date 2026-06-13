from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'people/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['usage_profile'] = self.request.user.usageprofile

        query = self.request.GET.get('q', '')
        context['query'] = query

        return context