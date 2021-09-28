# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import secrets
import string

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.templatetags.rest_framework import data

from accounts.models import UserProfile

from .forms import (Join, RegistrationForm, UpdateUserProfileform,
                    UserProfileform, UserUpdate, UploadBookForm)
from .models import classroom, EBooksModel
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import classroomSerializer, AccountPropertiesSerializer, pdfSerializer
from rest_framework import generics, permissions

"""""
class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""""


class classList(generics.ListCreateAPIView):
    queryset = classroom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = classroomSerializer


class classDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = classroom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = classroomSerializer


class pdfList(generics.ListCreateAPIView):
    queryset = EBooksModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = pdfSerializer


class pdfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EBooksModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = pdfSerializer

def index(request):
    data = None
    if request.user.is_authenticated:
        me = request.user.username
        you = f"Welcome {me}, to the classroom"
        messages.info(request, you)

        classes = classroom.objects.filter(
            user_profile__exact=request.user.profile
        )
        data = {'object_list': classes}

    return render(request, "class/index.html", data if data else None)


def create(request):
    return render(request, "class/upload.html")


def processing(request):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    if request.method == "POST":
        name = classroom()
        name.classname = request.POST.get('class_name')
        name.creator = request.user
        name.code = password
        name.save()
    return render(request, "class/create.html", {'password': password, 'creator': name.creator, 'name': name.classname})



def join(request):
    context = None
    if request.method == 'POST':
        form = Join(request.POST)
        if form.is_valid():
            passcode = form.cleaned_data['join']
            classrooms = classroom.objects.all()
            try:
                classroom_obj = classroom.objects.get(code=passcode)
            except classroom.DoesNotExist:
                messages.warning(
                    request, 'Wrong Classcode'
                )
                return render(request, "class/no.html")

            classroom_obj.user_profile.add(request.user.profile)
            messages.success(
                request, 'Welcome to the Classroom'
            )
            return render(
                request, "class/okay.html",
                {'classrooms': classrooms, 'pswd': passcode}
            )

    else:
        form = Join()
        context = {"form": form}

    messages.info(request, 'Enter the unique passcode below')
    return render(request, "class/join.html", context if context else None)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = UserProfileform(request.POST)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            description = profile_form.cleaned_data['Description']
            user = authenticate(username=username, password=password)
            login(request, user)
            profile = UserProfile.objects.get(user=user)
            profile.description = description
            profile.save()
            return redirect('index')
    else:
        form = RegistrationForm()
        profile_form = UserProfileform()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)


def pdfviewer(request):
    return render(request, "class/pdf_viewer.html")


def pdf(request):
    return render(request, "class/pdf-copy.html")


def classUI(request):
    return render(request, "class/classroom.html")


def profile(request):
    form = classroom.objects.all()
    context = {'form': form}
    return render(request, 'class/profile.html', context)


def StudentRegister(request):
    form = StudentRegistration

    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'registration/Student-register.html', context)


def home(request):
    return render(request, 'class/home.html')


def teacherProfile(request):
    return render(request, 'class/teacher-profile.html')


def BookUploadView(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadBookForm()
        context = {
            'form': form,
        }
    return render(request, 'class/file-uploader.html', context)
