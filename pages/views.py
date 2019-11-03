from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): # new
    template_name = 'about.html'


#from django.http import HttpResponse
#from django.shortcuts import render
#
# def homePageView(request):
#    return HttpResponse('Hello, World!')
