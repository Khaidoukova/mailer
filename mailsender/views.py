from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from mailsender.forms import ClientForm, MessageForm, MailingForm
from mailsender.models import Client, Mailing, Message, MailingLogs
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


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailsender:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()

        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailsender:index')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailsender:index')


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        # user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)

        return queryset



class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:index')
    permission_required = 'mailsender.change_mailing'

    def test_func(self):
        user = self.request.user
        mailing = self.get_object()
        if mailing.owner == user:
            return True
        else:
            return False


class MailingDetailView(DetailView):
    model = Mailing


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

class MailingLogsView(ListView):
    model = MailingLogs

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset





