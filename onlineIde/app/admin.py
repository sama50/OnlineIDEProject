from django.contrib import admin
from app.models import problem , UserProfile , ListOfProblem

class probleAdmin(admin.ModelAdmin):
    list_display = ('id','title','details','saveDate','sudoCode','funCall','input1','input2','input3','output1', 'output2','output3')
admin.site.register(problem,probleAdmin)

@admin.register(UserProfile)
class UserModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'userimag','name', 'locality', 'city', 'zipcode', 'collegeName']


@admin.register(ListOfProblem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id','user','problem']