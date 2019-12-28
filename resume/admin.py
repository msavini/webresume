from django.contrib import admin
from resume.models import CodingCourse, OtherCourse, Award, Skill, Work, Project
# Register your models here.

class CodingCourseAdmin(admin.ModelAdmin):
    pass
class OtherCourseAdmin(admin.ModelAdmin):
    pass
class AwardAdmin(admin.ModelAdmin):
    pass
class SkillAdmin(admin.ModelAdmin):
    pass
class WorkAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass
	
admin.site.register(CodingCourse, CodingCourseAdmin)
admin.site.register(OtherCourse, OtherCourseAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Project, ProjectAdmin)