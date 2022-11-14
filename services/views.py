from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from django.db.models import Count
from datetime import datetime, timedelta, time
import random
# Create your views here.

def Index(request):
    error = ""
    allcategory = Category.objects.all()
    person = Person.objects.all().values('category').annotate(total=Count('id'))
    '''if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"'''
    d = {'error': error,'person': person,'allcategory':allcategory}
    return render(request, 'index.html', d)


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def category(request):

    person = Person.objects.all().values('category').annotate(total=Count('id'))
    d = {'person': person}
    return render(request,'category.html',d)



def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('index')

    totalc = Category.objects.all().count()
    totalp = Person.objects.all().count()

    d = {'totalc':totalc,'totalp':totalp}
    return render(request,'admin_home.html',d)



def Logout(request):
    logout(request)
    return redirect('index')


def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        c = request.POST['confirmpassword']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'changepassword.html',d)


def add_category(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    if request.method=="POST":
        cn = request.POST['category']
        try:
            Category.objects.create(categoryname=cn)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_category.html', d)


def manage_category(request):
    if not request.user.is_authenticated:
        return redirect('index')
    category = Category.objects.all()
    d = {'category':category}
    return render(request, 'manage_category.html', d)


def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('manage_category')

def edit_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    category = Category.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        c = request.POST['category']
        category.categoryname = c
        try:
            category.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category}
    return render(request, 'edit_category.html',d)






def add_person(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    category = Category.objects.all()
    if request.method=="POST":
        cn = request.POST['category']
        n = request.POST['name']
        pic = request.FILES['propic']
        mn = request.POST['mobilenumber']
        ad = request.POST['address']
        ct = request.POST['city']
        #category1 = Category.objects.get(categoryname=cn)
        try:
            Person.objects.create(category=cn,name=n,picture=pic,mobileno=mn,address=ad,city=ct,regdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'category':category}
    return render(request, 'add_person.html', d)


def manage_person(request):
    if not request.user.is_authenticated:
        return redirect('login')
    person = Person.objects.all()
    d = {'person':person}
    return render(request, 'manage_person.html', d)


def delete_person(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    person = Person.objects.get(id=pid)
    person.delete()
    return redirect('manage_person')

def edit_person(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    person = Person.objects.get(id=pid)
    category = Category.objects.all()
    error = ""
    if request.method == 'POST':
        c = request.POST['category']
        n = request.POST['name']
        mn = request.POST['mobilenumber']
        a = request.POST['address']
        city = request.POST['city']

        #category1 = Category.objects.get(categoryname=c)
        person.category = c
        person.name = n
        person.mobileno = mn
        person.address = a
        person.city = city
        try:
            person.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'person':person,'category':category}
    return render(request, 'edit_person.html',d)



def change_image(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    person = Person.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        pic = request.FILES['newpic']
        person.picture = pic
        try:
            person.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'person':person}
    return render(request, 'change_image.html',d)


def serviceman_search(request):
    l = request.POST.get('location')
    c = request.POST.get('categories')
    try:
        person = Person.objects.filter(city=l,category=c)
    except:
        person = ""
    d = {'person': person,'l':l,'c':c}
    return render(request, 'serviceman_search.html',d)




def person_detail(request,pid):
    person = Person.objects.get(id=pid)

    d = {'person':person}
    return render(request, 'person_detail.html',d)

def category_detail(request,pid):
    person = Person.objects.filter(category=pid)

    d = {'person':person,'pid':pid}
    return render(request, 'category_detail.html',d)



