from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from qa.models import Question


# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def mainpg(request):
	qs = Question.objects.order_by('-id')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('mainpg')
	return render(request, 'main.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})

def question(request, pk):
	question = get_object_or_404(Question, id=pk)
	answers = question.answer_set.all()
	return render(request, 'question.html', {
		'question': question,
		'answers': answers,
	})

def popular(request):
	qs = Question.objects.order_by('-rating')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('popular') + '?page='
	return render(request, 'popular.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})
