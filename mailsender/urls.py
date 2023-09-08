from django.urls import path

from mailsender.apps import MailsenderConfig
from mailsender.views import MailingListView

app_name = MailsenderConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    #path('create_client/', create_client, name='create_client'),
    #path('create_mailing/', create_mailing, name='create_mailing'),
    #path('create_message/', create_message, name='create_message'),

]