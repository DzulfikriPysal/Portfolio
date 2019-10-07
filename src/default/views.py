from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {}
    return render(request, 'default/index.html', context)

def work(request):
    context = {}
    return render(request, 'default/work.html', context)


def about(request):
    context = {}
    return render(request, 'default/about.html', context)


def contact(request):
    context = {}
    return render(request, 'default/contact.html', context)


def portfolio_details(request):
    context = {}
    return render(request, 'default/portfolio_details.html', context)

def service(request):
    context = {}
    return render(request, 'default/services.html', context)

def portfolio(request):
    context = {}
    return render(request, 'default/portfolios.html', context)

def elements_path(request):
    context = {}
    return render(request, 'default/elements_path.html', context)