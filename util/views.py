from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import loginForm, UserForm
from .models import User


# def thanks(request):
#    return render(request,'userPage.html')
def saveUser(request):
    user = UserForm(request.POST)
    user.save(True)
    return HttpResponseRedirect('/')
    # return render(request,'home.html')


def signup(request):
    form = UserForm()
    context = {}
    context['form'] = form
    return render(request, "signup.html", context)


def homePage(request):
    form = loginForm(request.POST)
    context = {}
    context['form'] = form
    return render(request, 'home.html', context)


def findDisease(request):
    return render(request, "findDisease.html",{'nbar': 'findDisease'})


def prevDiagnosis(request):
    return render(request, 'prevDiagnosis.html',{'nbar': 'prevDiagnosis'})


def addNewDiagnosis(request):
    return render(request, 'addNewDiagnosis.html',{'nbar': 'addNewDiagnosis'})


def login(request):
    print("From login:", request.POST)
    user = {}

    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data['name']
            password1 = form.cleaned_data['password']

            userCount = User.objects.all().filter(name=name1, password=password1).count()

            print("post ", form.cleaned_data['name'])
            user["name"] = form.cleaned_data['name']
            print("pass ", form.cleaned_data['password'])

            if userCount != 1:
                print("Wrong user")
                messages.error(request, "Wrong user or password")
                return render(request, 'home.html')
            else:
                return render(request, 'userPage.html', {'user': user})

            # return HttpResponseRedirect('thanks/')

    # print(request.)
