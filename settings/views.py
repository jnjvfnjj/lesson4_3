from django.shortcuts import render
from settings.models import Settings, About, Program, Teacher

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    program = Program.objects.latest("id")
    teacher = Teacher.objects.latest("id")
    return render(request, "index.html", locals())