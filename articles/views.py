from django.http import HttpResponse
from django.shortcuts import render

def article_lists(request) :
	return render(request,'articles/lists.html')

