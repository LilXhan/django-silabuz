from django.shortcuts import render, redirect
from .models import Student, ClassRoom
from .formsexample import StudenForm
from .forms import ClassroomForm, StudentForm
from django.views.generic import View, TemplateView, CreateView, FormView, DeleteView
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
# para funciones
from django.contrib.auth.decorators import login_required
import json




def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')


@login_required
def classroom(request, id):
    context = {
        'students': Student.objects.filter(idClassroom_id=id)
    }

    return render(request, 'student/student.html', context)


class StudentForm(FormView):
    model = Student
    form_class = StudentForm
    template_name = 'student/create.html'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        student = Student.objects.create(**cleaned_data)
        student.save()
        return redirect('/')


class IndexClassroom(LoginRequiredMixin, View):
    def get(self, request):
        classrooms = []
        if request.session.get("classrooms") is not None:
            classrooms_session = json.loads(request.session.get("classrooms"))
            for classroom in classrooms_session:
                classrooms.append(classroom['fields'])
        else:
            classrooms = ClassRoom.objects.all()
            # convertir de queryset a json
            request.session["classrooms"] = serializers.serialize('json', classrooms)

        context = {
            'classrooms':classrooms
        }
        
        return render(request, 'management/index.html', context)


class IndexTemplateView(TemplateView):
    template_name = 'management/index.html'
    



class ManagementView(TemplateView):
    extra_context = {
        'classrooms': ClassRoom.objects.all() 
    }
    template_name = 'management/index.html'


    """ 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = ClassRoom.objects.all()
        return context
    """

class CreateClassroom(FormView):
    model = ClassRoom
    form_class = ClassroomForm
    template_name = 'management/create.html'
    success_url = '/'


    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        classroom = ClassRoom.objects.create(**cleaned_data)
        classroom.save()
        return redirect('/')


def DeleteClassroom(request, id):
    classroom = ClassRoom.objects.get(id=id)
    classroom.delete()
    return redirect('/')
































class CreateStudent(FormView):
    model = Student
    form_class = StudenForm
    template_name = 'form.html'
    success_url = "/"

    # para guardar la informacion existe lo que es una funcion llamada
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        student = Student.objects.create(**cleaned_data)
        student.save()
        return redirect('index')


class CreateStudents(View):

    def get(self, request):
        context = {
            'form': StudenForm
        }
        return render(request, 'form.html', context)
    
    def post(self, request):
        form = StudenForm(request.POST)
        # vamos a poder acceder a la informacion
        if form.is_valid():
            # como accedo a la info de los inputs
            cleaned_data = form.cleaned_data
            student = Student.objects.create(**cleaned_data)
            student.save()
            return redirect('index')
        else:
            print(form.errors)


class CreateIndexView(CreateView):
    template_name = 'index.html'
    model = Student
    fields = ['first_name', 'sur_name', 'born_date']
    extra_context = {
        'students': Student.objects.all()
    }


class TemplateIndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        'students': Student.objects.all()
    }


class Index(View):
    # tiene los metodos predefinidos
    
    def get(self, request):
        students = Student.objects.all()

        context = {
            'students': students
        }
    
        return render(request, 'index.html', context)


    def post(self, request):
        # logica para crear una persona

        Student.objects.create(name=request.POST["name"])

        return redirect('index')


def index(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    
    if request.method == 'GET':
        print('GET')

    elif request.method == 'POST':
        print('POST')
    

    return render(request, 'index.html', context)


