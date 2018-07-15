from django.db import models

class category(models.Model):
	category=models.CharField(max_length=100)
	
	def __str__(self):
		return(self.category)

class sub_category(models.Model):
	category=models.ForeignKey(category,on_delete=models.CASCADE)
	sub_cat=models.CharField(max_length=500)
	
	def __str__(self):
		return(self.sub_cat)
	
	
	
