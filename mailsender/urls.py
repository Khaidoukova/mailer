from django.urls import path

from mailsender.apps import MailsenderConfig

app_name = MailsenderConfig.name

urlpatterns = [
    #path('', MailsenderListView.as_view(), name='index'),
    #path('create_client/', create_client, name='create_client'),
    #path('create_mailing/', create_mailing, name='create_mailing'),

]