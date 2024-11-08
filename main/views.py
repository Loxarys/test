from django.shortcuts import render, redirect

def principal(request):

    return (render(request,'Landing.html'))