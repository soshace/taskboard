# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User

from website.forms import RegistrationForm, LoginForm
from website.models import UserProfile

# Create your views here.
def index(request):
    if request.user.is_authenticated() is False:
        reg_form = RegistrationForm(auto_id='reg_%s')
        login_form = LoginForm(auto_id='login_%s')

        c = {'reg_form' : reg_form, 'login_form': login_form, 'session': request.user}
        c.update(csrf(request))

        return render_to_response('index.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/profile/")

def ajax_register(request):
	if request.method != 'POST':
		return HttpResponse("NOTFOUND")

	reg_form = RegistrationForm(request.POST)
	if reg_form.is_valid():
		username = reg_form.cleaned_data['username']
		email = reg_form.cleaned_data['email']
		password = reg_form.cleaned_data['password']
		user_type = reg_form.cleaned_data['user_type']
		if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
			#checking for existing emails and usernames
			return HttpResponse("EXISTS")
		user = User.objects.create_user(username, email, password)
		user_profile = UserProfile(account=user, user_type=user_type)

		user.save()
		user_profile.save()

		return HttpResponse("OK")
	else:
		return HttpResponse("NOTVALID")

def profile(request):
    if request.user.is_authenticated() is False:
        return HttpResponse(request.user.username)
    else:
        return HttpResponse("OK")