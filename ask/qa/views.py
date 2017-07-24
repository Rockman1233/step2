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
