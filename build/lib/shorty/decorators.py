from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.functional import wraps
from shorty.models import Url
from shorty.utils import url_decode

__author__ = 'ogonbat'

def shorty_filter_url(view):
    @wraps(view)
    def inner(request, slug, *args, **kwargs):
        try:
            #search in personal SLUG
            url = Url.objects.get(personal_slug=slug)
        except Url.DoesNotExist:
            id_url = url_decode(slug)
            url = get_object_or_404(Url,id=id_url)
        if settings.SHORTY_MODERATE == True:
            #start moderation
            if url.is_banned:
                return HttpResponseRedirect(settings.SHORTY_BANNED)
            #pending link
            if url.is_pending:
                return HttpResponseRedirect(settings.SHORTY_PENDING)
            #refused link
            if url.is_refused:
                return HttpResponseRedirect(settings.SHORTY_REFUSED)
        return view(request,url,*args,**kwargs)
    return inner

def shorty_login_required(view):
    @wraps(view)
    def inner(request,*args,**kwargs):
        if settings.SHORTY_ANONYMOUS_ADD:
            if not request.user.is_authenticated():
                return HttpResponseRedirect(settings.LOGIN_URL)
        return view(request,*args,**kwargs)
    return inner