from django.http import HttpResponseRedirect
from django.template import Node
from django.template.defaulttags import url as _url
from django.template.defaulttags import register as _register
from django.conf import settings


def admin_redirect(request):
    return HttpResponseRedirect('/admin/')

class URLNodeRewriter(Node):
    def __init__(self, impl):
        self._impl = impl

    def render(self, context):
        url = self._impl.render(context)
        if url == '':
            # asvar usage
            return '' 
        else:
            return settings.APP_PREFIX + url

def url(parser, token):
    return URLNodeRewriter(_url(parser, token))
_register.tag(url)
