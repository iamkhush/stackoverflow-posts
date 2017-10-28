from django.conf.urls import url
from django.views.generic import TemplateView

from .views import PostListView, get_my_posts

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^posts/$', PostListView.as_view(), name='posts'),
    url(r'^get-my-posts/$', get_my_posts)
]
