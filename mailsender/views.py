import random
from blog.utils import blog_cache

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from blog.models import Blog
from mailsender.forms import ClientForm, MailingForm, ManagerUpdateForm
from mailsender.models import Client, Mailing, MailingLogs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class IndexView(TemplateView):
    template_name = 'mailsender/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mailing_count = Mailing.objects.count()
        context['mailing_count'] = mailing_count

        active_mailings = Mailing.objects.filter(status='created').count()
        context['active_mailings'] = active_mailings

        unique_clients = Client.objects.count()
        context['unique_clients'] = unique_clients

        all_blogs = list(blog_cache())
        print(all_blogs)

        if len(all_blogs) >= 3:
            random_blogs = random.sample(all_blogs, 3)
        else:
            random_blogs = all_blogs

        context['random_blogs'] = random_blogs

        return context


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailsender:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailsender:index')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailsender:index')


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Managers').exists() or user.is_superuser:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(
                owner=user.pk
            )
        return queryset


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:index')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailsender:index')


class MailingDetailView(DetailView):
    model = Mailing


class MailingLogsView(LoginRequiredMixin, ListView):
    model = MailingLogs
    template_name = 'mailsender/mailinglog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset


class MailingManagerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = ManagerUpdateForm
    success_url = reverse_lazy('mailsender:mailing_list')
    permission_required = 'mailsender.change_mailing_status'







