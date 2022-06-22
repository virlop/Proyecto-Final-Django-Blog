import django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from virginiaBlog.models import BlogModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'virginiaBlog/blog_crear_cuenta_form.html'
    success_url = reverse_lazy('virginiaBlog_login')
    form_class = UserCreationForm
    success_message = "Your profile was created successfully"

class BlogList(ListView):

    model = BlogModel
    template_name = "virginiaBlog/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "virginiaBlog/blog_detail.html"

#tener en cuenta nomenglaturas de templates
class BlogCreate(LoginRequiredMixin,CreateView):

    model = BlogModel
    success_url = reverse_lazy("virginiaBlog_list") #a donde va si es exitosa la carga
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"] #campos del formulario para la creacion


class BlogUpdate(LoginRequiredMixin,UpdateView):

    model = BlogModel
    success_url = reverse_lazy("virginiaBlog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogDelete(LoginRequiredMixin,DeleteView):

    model = BlogModel
    success_url = reverse_lazy("virginiaBlog_list")
    
class BlogLogin(LoginView):
    template_name = 'virginiaBlog/blog_login.html'
    next_page = reverse_lazy('virginiaBlog_list')

class BlogLogout(LogoutView):
    template_name = 'virginiaBlog/blog_logout.html'
