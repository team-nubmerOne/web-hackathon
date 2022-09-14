"""
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Choice,Question
from django.urls import reverse


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list' : latest_question_list}

    return render(request,'polls/index.html',context)



'''
def index(request):
    #return HttpResponse("Hello,world.You're at the polls index.");
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context,request))
'''

def detail(request,question_id):    
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist")
    return render(request,'polls/detail.html',{'question':question})
    '''
    question = get_object_or_404(Question,pk=question_id);
    return render(request,'polls/detail.html',{'question':question})
    
    #return HttpResponse("Your're looking at question %s."%question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def printText():
        arr = np.empty((0,3), int)                     #기상청 #실제온도
        arr = np.append(arr, np.array([['2022-07-01', 28, 31]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-02', 27, 32]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-03', 24, 30]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-04', 28, 35]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-05', 31, 30]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-06', 29, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-07', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-08', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-09', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-10', 27, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-11', 28, 30]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-12', 25, 27]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-13', 31, 30]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-14', 30, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-15', 25, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-16', 30, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-17', 32, 31]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-18', 29, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-19', 28, 30]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-20', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-21', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-22', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-23', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-24', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-25', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-26', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-27', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-28', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-29', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-30', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-07-31', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-01', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-02', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-03', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-04', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-05', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-06', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-07', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-08', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-09', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-10', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-11', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-12', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-13', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-14', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-15', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-16', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-17', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-18', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-19', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-20', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-21', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-22', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-23', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-24', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-25', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-26', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-27', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-28', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-29', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-30', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-08-31', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-01', 27, 26]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-02', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-03', 31, 32]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-04', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-05', 30, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-06', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-07', 27, 26]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-08', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-09', 30, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-10', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-11', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-12', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-13', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-14', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-15', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-16', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-17', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-18', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-19', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-20', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-21', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-22', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-23', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-24', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-25', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-26', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-27', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-28', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-29', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-09-30', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-10-01', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-10-02', 28, 29]]), axis=0)
        arr = np.append(arr, np.array([['2022-10-03', 31, 28]]), axis=0)
        arr = np.append(arr, np.array([['2022-10-04', 26, 24]]), axis=0)
        arr = np.append(arr, np.array([['2022-10-05', 28, 29]]), axis=0)

        df = pd.DataFrame(arr,columns=['날짜','기상청','실제온도'])
        # csv파일을 전부 긁어와서 서울시의 1년치 날짜별 기온을 전부 기록해서 모델링하고
        x = df["날짜"]
        y = df["기상청"]
        z = df["실제온도"]
        #사실상 date는 제외하고 temp와 sales의 상관관계를 예측하는 모델이니
        #date는 명시만 해둡니다
        line_fitter = LinearRegression()
        line_fitter.fit(y.values.reshape(-1,1), z)
        #모델링후 아래에서 모델을  사용합니다
        print("2022-07-11 의 경우엔 : ",line_fitter.predict([[26]]))
        print("2022-07-12 의 경우엔 : ",line_fitter.predict([[24]]))
        print("2022-07-13 의 경우엔 : ",line_fitter.predict([[39]]))
        #예측결과를 출력해줍니다

    printText()

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))