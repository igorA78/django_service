from django.conf import settings
from django.core.cache import cache

from blog.models import Article


def get_cached_articles_list():
    if settings.CACHE_ENABLED:
        key = 'articles_list'
        articles_list = cache.get(key)
        if articles_list is None:
            articles_list = Article.objects.all()
            cache.set(key, articles_list)
    else:
        articles_list = Article.objects.all()

    return articles_list
