#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect
import hashlib

def encrypt(userID, password):
  first_md5 = hashlib.md5()
  first_md5.update(str(password))
  salt = first_md5.hexdigest()
  second_md5 = hashlib.md5()
  second_md5.update(str(userID) + salt)
  return second_md5.hexdigest()

@csrf_exempt
def login(request):
  if request.method == 'POST':
    '''userID = request.POST['userID']
    password = request.POST['password']'''
    userID = request.POST['userID']
    password = request.POST['password']
    password = encrypt(userID, password)
    try:
      user = User.objects.get(userID = userID)
      if user.password != password:
        return HttpResponse("password error!")
      else:
        request.session["userID"] = userID
        return HttpResponse("success")
    except:
      return HttpResponse(userID+" does not exsits")
  else:
    login_out = request.GET.get('login_out')
    if login_out == "true":
        del request.session['userID']
    try:
      user = User.objects.get(userID = request.session['userID'])
      return HttpResponseRedirect("/index/problemList")
    except:
      return render(request, 'cugbacm/login.html', {})
