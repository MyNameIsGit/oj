#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def contestRankList(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
    # todo: get rank_list
    return render(request,
                 'cugbacm/contestRankList.html',
                 {
                    'userID':request.session['userID'],
                    'contest': Contest.objects.get(contestID = contest_id)
                 })
  except:
    
    return render(request,
                 'cugbacm/contestRankList.html',
                 {
                    'userID':request.session['userID'],
                    #'contest': Contest.objects.get(contestID = contest_id)
                 })
    return HttpResponseRedirect("/index/login")
