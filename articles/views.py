from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles

def article_lists(request) :
	articles = Articles.objects.all().order_by('date')
	return render(request,'articles/lists.html',{'arti' : articles})

def article_details(request,slug) :
	article = Articles.objects.get(slug=slug)
	return render(request,'articles/details.html',{'article' : article})