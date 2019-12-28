import json

from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


from .models import CodingCourse,OtherCourse,Award,Skill,Work,Project


def index(request):
	context = {
	"current": 'index',
	}
	return render(request, "index.html", context)


def about(request):
	context = {
	"current": 'about',
	}
	return render(request, "about.html", context)
	
def portfolio(request):
	context = {
	"current": 'portfolio',
	}
	return render(request, "portfolio.html", context)
	
def webresume(request):
	cCourse = CodingCourse.objects.first()
	oCourse = OtherCourse.objects.first()
	cAward = Award.objects.first()
	cSkill = Skill.objects.first()
	cProject = Project.objects.first()
	cWork = Work.objects.first()
	
	CodingCourses = CodingCourse.objects.all()
	OtherCourses = OtherCourse.objects.all()
	Awards = Award.objects.all()
	Skills = Skill.objects.all().order_by('-proficiency')
	Projects = Project.objects.all()
	Works = Work.objects.all()
	context = {
	"cCourse" : cCourse,
	"oCourse" : oCourse,
	"cAward" : cAward,

	"cProject" : cProject,
	"cWork" : cWork,
	"CodingCourses": CodingCourses,
	"OtherCourses": OtherCourses,
	"Awards": Awards,
	"Skills": Skills,
	"Works": Works,
	"Projects": Projects,
	"current": 'webresume',
	"show_item":'none'
	}
	return render(request, "resume.html", context)
	
def webresume_cCourse(request, pk, slug):
	cCourse = CodingCourse.objects.get(pk=pk)
	oCourse = OtherCourse.objects.first()
	cAward = Award.objects.first()
	cProject = Project.objects.first()
	cWork = Work.objects.first()
	
	CodingCourses = CodingCourse.objects.all()
	OtherCourses = OtherCourse.objects.all()
	Awards = Award.objects.all()
	Skills = Skill.objects.all().order_by('-proficiency')
	Projects = Project.objects.all()
	Works = Work.objects.all()
	context = {
	"cCourse" : cCourse,
	"oCourse" : oCourse,
	"cAward" : cAward,
	"cProject" : cProject,
	"cWork" : cWork,
	"currentCourse" : cCourse,
	"CodingCourses": CodingCourses,
	"OtherCourses": OtherCourses,
	"Awards": Awards,
	"Skills": Skills,
	"Works": Works,
	"Projects": Projects,
	"current": 'webresume',
	"show_item":'cCourse'
	}
	return render(request, "resume.html", context)
	
def webresume_oCourse(request, pk, slug):
	cCourse = CodingCourse.objects.first()
	oCourse = OtherCourse.objects.get(pk=pk)
	cAward = Award.objects.first()
	cProject = Project.objects.first()
	cWork = Work.objects.first()
	
	CodingCourses = CodingCourse.objects.all()
	OtherCourses = OtherCourse.objects.all()
	Awards = Award.objects.all()
	Skills = Skill.objects.all().order_by('-proficiency')
	Projects = Project.objects.all()
	Works = Work.objects.all()
	context = {
	"cCourse" : cCourse,
	"oCourse" : oCourse,
	"cAward" : cAward,
	"cProject" : cProject,
	"cWork" : cWork,
	"currentCourse" : cCourse,
	"CodingCourses": CodingCourses,
	"OtherCourses": OtherCourses,
	"Awards": Awards,
	"Skills": Skills,
	"Works": Works,
	"Projects": Projects,
	"current": 'webresume',
	"show_item":'oCourse'
	}
	return render(request, "resume.html", context)
	
def webresume_cAward(request, pk, slug):
	cCourse = CodingCourse.objects.first()
	oCourse = OtherCourse.objects.first()
	cAward = Award.objects.get(pk=pk)
	cProject = Project.objects.first()
	cWork = Work.objects.first()
	
	CodingCourses = CodingCourse.objects.all()
	OtherCourses = OtherCourse.objects.all()
	Awards = Award.objects.all()
	Skills = Skill.objects.all().order_by('-proficiency')
	Projects = Project.objects.all()
	Works = Work.objects.all()
	context = {
	"cCourse" : cCourse,
	"oCourse" : oCourse,
	"cAward" : cAward,
	"cProject" : cProject,
	"cWork" : cWork,
	"currentCourse" : cCourse,
	"CodingCourses": CodingCourses,
	"OtherCourses": OtherCourses,
	"Awards": Awards,
	"Skills": Skills,
	"Works": Works,
	"Projects": Projects,
	"current": 'webresume',
	"show_item":'cAward'
	}
	return render(request, "resume.html", context)

def webresume_cProject(request, pk, slug):
	cCourse = CodingCourse.objects.first()
	oCourse = OtherCourse.objects.first()
	cAward = Award.objects.first()
	cProject = Project.objects.get(pk=pk)
	cWork = Work.objects.first()
	
	CodingCourses = CodingCourse.objects.all()
	OtherCourses = OtherCourse.objects.all()
	Awards = Award.objects.all()
	Skills = Skill.objects.all().order_by('-proficiency')
	Projects = Project.objects.all()
	Works = Work.objects.all()
	context = {
	"cCourse" : cCourse,
	"oCourse" : oCourse,
	"cAward" : cAward,
	"cProject" : cProject,
	"cWork" : cWork,
	"currentCourse" : cCourse,
	"CodingCourses": CodingCourses,
	"OtherCourses": OtherCourses,
	"Awards": Awards,
	"Skills": Skills,
	"Works": Works,
	"Projects": Projects,
	"current": 'webresume',
	"show_item":'cProject'
	}
	return render(request, "resume.html", context)

def webresume_cWork(request, pk, slug):
	cCourse = CodingCourse.objects.first()
	oCourse = OtherCourse.objects.first()
	cAward = Award.objects.first()
	cProject = Project.objects.first()
	cWork = Work.objects.get(pk-pk)
	
	CodingCourses = CodingCourse.objects.all()
	OtherCourses = OtherCourse.objects.all()
	Awards = Award.objects.all()
	Skills = Skill.objects.all().order_by('-proficiency')
	Projects = Project.objects.all()
	Works = Work.objects.all()
	context = {
	"cCourse" : cCourse,
	"oCourse" : oCourse,
	"cAward" : cAward,
	"cProject" : cProject,
	"cWork" : cWork,
	"currentCourse" : cCourse,
	"CodingCourses": CodingCourses,
	"OtherCourses": OtherCourses,
	"Awards": Awards,
	"Skills": Skills,
	"Works": Works,
	"Projects": Projects,
	"current": 'webresume',
	"show_item":'cWork'
	}
	return render(request, "resume.html", context)

def contact(request):
	context = {
	"current": 'contact',
	}
	return render(request, "contact.html", context)
	
