# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from webapp.models import Company


def index(request):
    companies = Company.objects.all()
    print(companies)
    context = {'companies': companies}
    return render(request, 'webapp/base.html', context=context)


# def company(request):
#     companies = Company.objects.all().order_by('name')
#     context = {'companies': companies}
#     return render(request, 'webapp/company.html', context=context)

class CompanyView(LoginRequiredMixin, ListView):
    template_name = 'webapp/company.html'
    queryset = Company.objects.all().order_by('name')
    context_object_name = 'companies'
    # login_url = '/login/'


# def company_detail(request, pk):
#     company = Company.objects.get(pk=pk)
#     context = {'company': company}
#     return render(request, 'webapp/company_detail.html', context=context)

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'webapp/company_detail.html'

# 1
# def about(request):
#     return HttpResponse('<h2>This is about page</h2>')
# 2
# def about(request):
#     return render(request, 'webapp/about.html')

class AboutPageView(TemplateView):
    template_name = 'webapp/about.html'

class CRMLogin(LoginView):
    template_name = 'webapp/login.html'
    redirect_field_name = True