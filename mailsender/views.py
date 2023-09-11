from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from mailsender.forms import ClientForm
from mailsender.models import Client, Mailing, Message, MailingLogs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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




class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'sending_time', 'frequency', 'status', 'client')




