# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from webapp.forms import OfficeForm
from webapp.models import Company, Office


def index(request):
    companies = Company.objects.all()
    print(companies)
    context = {'companies': companies}
    return render(request, 'webapp/index.html', context=context)


class CompanyView(ListView):
    """Company View"""
    template_name = 'webapp/company.html'
    context_object_name = 'companies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        paginator = Paginator(context['object_list'], 3)
        page_objs = paginator.get_page(page_number)
        context['page_objs'] = page_objs
        context['title'] = 'Компании'
        return super().get_context_data(**context)

    def get_queryset(self):
        return Company.objects.all()

# def company_detail(request, pk):
#     company = Company.objects.get(pk=pk)
#     context = {'company': company}
#
#     if request.method == 'POST':
#         form = OfficeForm(data=request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             address = form.cleaned_data['address']
#             Office.objects.create(name=name, address=address, company_id=pk)
#         form = OfficeForm()
#         context['form'] = form
#     else:
#         form = OfficeForm()
#         context['form'] = form
#
#     return render(request, 'webapp/company_detail.html', context=context)


class CompanyDetailView(FormMixin, DetailView):
    model = Company
    form_class = OfficeForm
    template_name = 'webapp/company_detail.html'
    # success_url = reverse_lazy('company_detail')

    def get_success_url(self):
        return reverse_lazy('company_detail', args=[self.object.id])

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        context['title'] = 'Компания'

        return super().get_context_data(**context)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.render_to_response(
            self.get_context_data(object=self.object, form=form)
        )


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            Office.objects.create(name=name, address=address, company_id=self.object.pk)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# 1
# def about(request):
#     return HttpResponse('<h2>This is about page</h2>')
# 2
# def about(request):
#     return render(request, 'webapp/about.html')

class AboutPageView(TemplateView):
    template_name = 'webapp/about.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['title'] = 'О нас'
        return super().get_context_data(**context)


class CRMLogin(LoginView):
    template_name = 'webapp/login.html'
    redirect_field_name = True