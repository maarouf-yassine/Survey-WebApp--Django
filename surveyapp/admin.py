from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_header = "Surveyor Admin"
admin.site.site_title = "Surveyor"


admin.site.register(Survey)
admin.site.register(User)
admin.site.register(SubmittedSurveys)
admin.site.register(Category)

