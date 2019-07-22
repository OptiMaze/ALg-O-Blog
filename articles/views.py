from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from .import forms


def article_lists(request) :
	articles = Articles.objects.all().order_by('date')
	return render(request,'articles/lists.html',{'arti' : articles})

def article_details(request,slug) :
	article = Articles.objects.get(slug=slug)
	return render(request,'articles/details.html',{'article' : article})

@login_required(login_url= "/accounts/login")
def create(request):
	if request.method == 'POST' :
		form = forms.CreateArticles(request.POST)
		if form.is_valid():
			instance = form.save(commit  = False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')
		else :
			form  = forms.CreateArticles()
			return render(request,'articles/create.html',{'form' : form})
	else :
		form  = forms.CreateArticles()
		return render(request,'articles/create.html',{'form' : form})