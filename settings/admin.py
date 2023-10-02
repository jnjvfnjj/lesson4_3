from django.contrib import admin
from settings.models import Settings, About, Program, Teacher

# Register your models here.
admin.site.register(Settings)
admin.site.register(About)
admin.site.register(Program)
admin.site.register(Teacher)