from django.urls import path

from main.apps import MainConfig
from main.views import MainListView

app_name = MainConfig.name

urlpatterns = [
    path('', MainListView.as_view(), name='index')
]