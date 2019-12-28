from django.db import models
from django.conf import settings
from django.utils.text import slugify


class CodingCourse(models.Model):

	title = models.CharField(max_length = 200)			#name of the course
	slug = models.SlugField(max_length = 100)
	languages = models.CharField(max_length = 200) 		#languages taught in course
	description = models.TextField(null=True)			#course description
	location = models.CharField(max_length = 200)		#where the course was taken
	
	def __str__(self):
		return self.title

	
class OtherCourse(models.Model):

	title = models.CharField(max_length = 200)			#name of the course
	slug = models.SlugField(max_length = 100)
	description = models.TextField(null=True)			#course description
	location = models.CharField(max_length = 200)		#where the course was taken
	
	def __str__(self):
		return self.title


class Award(models.Model):

	title = models.CharField(max_length = 200)			#name of the award
	slug = models.SlugField(max_length = 100)
	description = models.TextField(null=True)			#award description 
	
	def __str__(self):
		return self.title


class Skill(models.Model):
	
	title = models.CharField(max_length = 200)			#skill
	type = models.CharField(max_length = 30)			#type: "technical", "social"
	proficiency = models.PositiveSmallIntegerField(default=1)	#proficiency: 100 being most
	
	def __str__(self):
		return self.title


class Work(models.Model):

	employer = models.CharField(max_length = 200)		#name of company / employer
	slug = models.SlugField(max_length = 100)
	duration = models.PositiveSmallIntegerField(default=1)	#time spent with employer
	responsibilities = models.TextField(null=True)		#responsibilities in brief
	
	def __str__(self):
		return self.employer

	
class Project(models.Model):
	title = models.CharField(max_length = 200)			#name of project
	slug = models.SlugField(max_length = 100)
	description = models.TextField(null=True)			#description of project
	link = models.URLField(max_length=255,null=True)	#link to project
	date = models.DateField(auto_now=False, auto_now_add=False)	#date
	collaborators = models.TextField(null=True)			#list of collaborators
	
	def __str__(self):
		return self.title

