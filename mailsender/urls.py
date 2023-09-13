from django.urls import path

from mailsender.apps import MailsenderConfig
from mailsender.views import MailingListView, ClientCreateView, MailingCreateView, IndexView, MessageCreateView, \
    ClientUpdateView, MailingUpdateView, MessageUpdateView

app_name = MailsenderConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('edit_mailing/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('edit_message/<int:pk>', MessageUpdateView.as_view(), name='message_update'),

    #path('create_message/', create_message, name='create_message'),

]