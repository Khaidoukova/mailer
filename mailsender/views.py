from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from mailsender.forms import ClientForm, MailingForm, ManagerUpdateForm
from mailsender.models import Client, Mailing, MailingLogs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class IndexView(TemplateView):
    template_name = 'mailsender/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        if user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(
                owner=user.pk
            )
        return queryset


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:index')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


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





