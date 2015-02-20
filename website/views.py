# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

from website.forms import RegistrationForm, LoginForm, PostTaskForm, TakeTaskForm, ChangeCommissionForm
from website.models import UserProfile, Task, TaskBoardSystem

# Create your views here.
def index(request):
    """ View on main page / """
    if request.user.is_authenticated() is False:
        reg_form = RegistrationForm(auto_id='reg_%s')
        login_form = LoginForm(auto_id='login_%s')

        c = {'reg_form' : reg_form, 'login_form': login_form, 'session': request.user}
        c.update(csrf(request))

        return render_to_response('index.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/profile/")

def ajax_register(request):
    """ AJAX regsiter procedure """
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

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(account=request.user)
    except ObjectDoesNotExist:
        user_profile = UserProfile(account=request.user)
        return HttpResponse("UserProfile doesn't exist!")

    if user_profile.user_type == 0: #customer
        count_task = Task.objects.filter(author=request.user).count()
        request.session['user_type'] = "customer"
    else:
        count_task = Task.objects.filter(executor=request.user).count()
        request.session['user_type'] = "executor"

    c = {'username': request.user, 'email': request.user.email, 'user_type': user_profile.user_type, 'cash': user_profile.cash, 'count_task': count_task}
    c.update(csrf(request))

    return render_to_response('profile.html', c, context_instance=RequestContext(request))

@login_required
def post(request):
    post_task_form = PostTaskForm(auto_id='post_task_%s')

    c = {'post_form': post_task_form, 'username': request.user, 'email': request.user.email, 'user_type': request.session.get('user_type')}

    return render_to_response('post.html', c, context_instance=RequestContext(request))

@login_required
def ajax_post_task(request):
    """ AJAX posting task procedure """
    if request.method != 'POST':
        return HttpResponse("NOTFOUND")

    post_task_form = PostTaskForm(request.POST)
    if post_task_form.is_valid():
        title = post_task_form.cleaned_data['title']
        description = post_task_form.cleaned_data['description']
        cost = post_task_form.cleaned_data['cost']

        task = Task(author=request.user, title=title, description=description, cost=cost)
        task.save()

        return HttpResponse("OK")
    else:
        return HttpResponse("NOTVALID")

def ajax_login(request):
    """ AJAX login procedure """
    if request.method != 'POST':
        return HttpResponse("NOTFOUND")

    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        try:
            user = authenticate(username=username, password=password)
            login(request, user)
        except Exception, e:
            return HttpResponse("CANT")
        return HttpResponse("OK")
    else:
        return HttpResponse("NOTVALID")

def ajax_logout(request):
    """ AJAX logout via POST method """
    try:
        logout(request)
    except Exception, e:
        return HttpResponse("CANT")
    return HttpResponseRedirect("/")

@login_required
def feed(request):
    """ Showing feed with tasks for executors"""
    try:
        tasks = Task.objects.filter(executor=None)
    except ObjectDoesNotExist:
        return HttpResponse("UserProfile doesn't exist!")

    take_task_form = TakeTaskForm(auto_id='take_task_%s')
    c = {'tasks': tasks, 'email': request.user.email, 'take_task_form': take_task_form, 'user_type': request.session.get('user_type')}
    c.update(csrf(request))

    return render_to_response('feed.html', c, context_instance=RequestContext(request))

@login_required
def ajax_take_task(request, task_number):
    """ Taking customer task with number """
    #сначала проверяем, если есть карточка, потом свободна ли она, потом получаем + обновляем данные
    try:
        task = Task.objects.get(pk=task_number)
    except ObjectDoesNotExist:
        return HttpResponse("NOSUCHTASK")
    if task.executor != None:
        return HttpResponse("OCCUPIED")
    task.executor = request.user
    task.save()

    #get firstly commission amount or create default 10%
    try:
        task_board_system = TaskBoardSystem.objects.get(id=1)
    except ObjectDoesNotExist:
        task_board_system = TaskBoardSystem(commission=10)
        task_board_system.save()
    commission_amount = task_board_system.commission

    try:
        user_profile = UserProfile.objects.get(account=request.user)
        user_profile.cash += (((100.0 - commission_amount)/100.0) * task.cost)
        user_profile.save()
    except ObjectDoesNotExist:
        return HttpResponse("NOWITHDRAWAL")

    return HttpResponse("OK")

@staff_member_required
def commission(request):
    """ Changing commission only for staff member """
    commission_form = ChangeCommissionForm(auto_id='commission_%s')

    c = {'commission_form' : commission_form, 'session': request.user}
    c.update(csrf(request))

    return render_to_response('commission.html', c, context_instance=RequestContext(request))

@staff_member_required
def commission_change(request):
    """ Changing commission or create table row """
    commission_form = ChangeCommissionForm(request.POST)

    if not commission_form.is_valid():
        return HttpResponse("FORM IS INCORRECT!")
    commission = commission_form.cleaned_data['commission']

    try:
        task_board_system = TaskBoardSystem.objects.get(id=1)
        task_board_system.commission = commission
        task_board_system.save()
    except ObjectDoesNotExist:
        task_board_system = TaskBoardSystem(commission=commission)
        task_board_system.save()
    return HttpResponse("NEW COMMISSION IS SAVED")