from django.shortcuts import render
from django.http import HttpResponse

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
