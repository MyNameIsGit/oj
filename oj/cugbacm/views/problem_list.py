#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def problemList(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
    problems = Problem.objects.all()
    if request.method == 'POST':
      problemID = request.POST['problemID']
      problemTitle = request.POST['problemTitle']
      problemAuthor = request.POST['problemAuthor']
      try:
        if problemID.strip():
          problems = problems.filter(problemID__contains = problemID)
        if problemTitle.strip():
          problems = problems.filter(title__contains = problemTitle)
        if problemAuthor.strip():
          problems = problems.filter(author__contains = problemAuthor)
        return render(
          request, 
          'cugbacm/problemList.html', 
          {
            'problems': problems, 
            'userID': request.session["userID"],
            'problemID': problemID,
            'problemTitle': problemTitle,
            'problemAuthor': problemAuthor
          }
        )
      except:
        return render(request, 'cugbacm/problemList.html', {'problems': {}, 'userID':request.session["userID"]})
    else:
      return render(request, 'cugbacm/problemList.html', {'problems': problems, 'userID':request.session["userID"]})
  except:
    return HttpResponseRedirect("/index/login")
