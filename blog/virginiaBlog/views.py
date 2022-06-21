from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from virginiaBlog.models import BlogModel


class BlogList(ListView):

    model = BlogModel
    template_name = "virginiaBlog/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "virginiaBlog/blog_detail.html"


class BlogCreate(CreateView):

    model = BlogModel
    success_url = reverse_lazy("virginiaBlog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogUpdate(UpdateView):

    model = BlogModel
    success_url = reverse_lazy("virginiaBlog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogDelete(DeleteView):

    model = BlogModel
    success_url = reverse_lazy("virginiaBlog_list")
