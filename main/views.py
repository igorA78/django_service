from django.views.generic import ListView

from blog.models import Article
from blog.services import get_cached_articles_list
from mailings.models import Mailing, Client


class MainListView(ListView):
    model = Article
    template_name = 'main/index.html'

    def get_queryset(self):
        return get_cached_articles_list()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].order_by('?')[:3]
        mailings_count = len(Mailing.objects.all())
        mailings_active_count = len(Mailing.objects.filter(status='started').all())
        clients_count = len(Client.objects.values('email').distinct())
        context['mailings_count'] = mailings_count
        context['mailings_active_count'] = mailings_active_count
        context['clients_count'] = clients_count
        return context
