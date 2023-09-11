from django.urls import path

from mailsender.apps import MailsenderConfig
from mailsender.views import MailingListView, ClientCreateView, MailingCreateView

app_name = MailsenderConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    
    #path('create_message/', create_message, name='create_message'),

]