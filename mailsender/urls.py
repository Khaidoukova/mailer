from django.urls import path

from mailsender.apps import MailsenderConfig
from mailsender.views import MailingListView, ClientCreateView, MailingCreateView, IndexView, \
    ClientUpdateView, MailingUpdateView, MailingDeleteView, ClientDeleteView, MailingDetailView, MailingLogsView, \
    MailingManagerUpdateView, mailing_logs

app_name = MailsenderConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),

    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('edit_mailing/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete_mailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('mailing_detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailinglogs', MailingLogsView.as_view(), name='mailinglogs'),
    path('manager_edit_mailing/<int:pk>', MailingManagerUpdateView.as_view(), name='manager_mailing_update'),
]