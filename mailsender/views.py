from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from mailsender.models import Client, Mailing, Message, MailingLogs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('sending_time', 'frequency', 'status')




