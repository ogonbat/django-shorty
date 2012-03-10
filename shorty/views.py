from django.http import HttpResponsePermanentRedirect

#method for url redirection
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from shorty.decorators import shorty_filter_url, shorty_login_required
from shorty.forms import Private_Form, Shorty_Form
from shorty.models import Url, Pslug
from shorty.utils import url_encode

@shorty_filter_url
def shorty_url(request,url_object,private_template='shorty/private.html'):
    """ Usage
        urlpatterns = patterns('',
                url(r'^(?P<slug>[\a-zA-Z0-9\-]+)/$','shorty.views.shorty_url',{'private_template':'your_private_template.html'},name="shorty_url"),
                )
    """
    if url_object.private == True:
        #check the form submission
        if request.method == 'POST':
            #this is the private form post
            form = Private_Form(data=request.POST)
            if form.is_valid():
                #check the private password
                if request.POST.get('private_password','') == url_object.private_password:
                    return HttpResponsePermanentRedirect(url_object.url_field)
            else:
                data_context = {
                    'shorty_form': form
                }
                return render_to_response(private_template, data_context,context_instance=RequestContext(request))
        else:
            form = Private_Form()
        data_context = {
            'shorty_form': form
        }
        return render_to_response(private_template, data_context,context_instance=RequestContext(request))
    return HttpResponsePermanentRedirect(url_object.url_field)

@shorty_login_required
def add_shorty_url(request,shorty_template='shorty/add.html'):
    """ Usage
        for example put the add_shorty_url to the home page
        urlpatterns = patterns('',
                url(r'^/?$','shorty.views.add_shorty_url',{'shorty_template':'your_private_template.html'},name="add_shorty_url"),
                )
    """
    if request.method == 'POST':
        #added new link
        form = Shorty_Form(data=request.POST)
        if form.is_valid():
            #the form is valid, add new form
            model_shorty = Url()
            if request.user.is_authenticated():
                model_shorty.user = request.user
            model_shorty.url_field = request.POST.get('link_url','')
            model_shorty.status = 'Active'
            model_shorty.save()
            if request.POST.get('personal_slug'):
                short_url = request.POST.get('personal_slug')
            else:
                short_url = url_encode(model_shorty.id)
            data_context = {
                'shorty_form': form,
                'url_slug': short_url,
            }
        else:
            data_context = {
                'shorty_form': form,
            }
        return render_to_response(shorty_template,data_context,context_instance=RequestContext(request))
    else:
        form = Shorty_Form()
        data_context = {
            'shorty_form': form
        }
        return render_to_response(shorty_template,data_context,context_instance=RequestContext(request))
