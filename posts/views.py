from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

import requests


class PostListView(TemplateView):
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # check UID to be number
        user_id = self.request.GET.get('uid')
        query_params = {
            'site': 'stackoverflow',
            'sort': 'activity',
            'order': 'desc',
            # put check for page to be a number
            'page': int(self.request.GET.get('page', 1)),
            'pagesize': 25
        }
        url = 'https://api.stackexchange.com/2.2/users/%s/posts' % user_id
        resp = requests.get(url, params=query_params)
        # should check error conditions here
        context['items'] = resp.json()['items']
        context['next'] = resp.json().get('has_more', False) and query_params['page'] + 1
        if query_params['page'] > 1:
            context['previous'] = query_params['page'] - 1
        return context


def get_my_posts(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/?message=Something+Went+Wrong')
    # get SO ID
    stackoverflow_uid = request.user.social_auth.all()[0].uid
    return HttpResponseRedirect('/posts/?uid=%s' % stackoverflow_uid)
