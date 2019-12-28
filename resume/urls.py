from django.contrib import admin 
from django.urls import path, re_path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from django.conf.urls import include

urlpatterns = [
    path("", views.index, name="index"),
	path("about", views.about, name="about"),
	path("portfolio", views.portfolio, name="portfolio"),
	
	path("resume/cscourse/<int:pk>-<slug:slug>", views.webresume_cCourse, name="webresume_cCourse"),
	path("resume/ocourse/<int:pk>-<slug:slug>", views.webresume_oCourse, name="webresume_oCourse"),
	path("resume/award/<int:pk>-<slug:slug>", views.webresume_cAward, name="webresume_cAward"),
	
	path("resume", views.webresume, name="webresume"),
	path("contact", views.contact, name="contact")
]