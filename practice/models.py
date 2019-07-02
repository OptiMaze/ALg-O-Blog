from django.db import models

class Practice(models.Model) :
	a = models.CharField(max_length = 30)
	b = models.DateTimeField(auto_now_add = True)
	c = models.TextField()
	d = models.IntegerField()

	def __str__(self) :
		return self.a

class AnotherOne(models.Model) :
	a = models.CharField(max_length = 30)
	b = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.a
		