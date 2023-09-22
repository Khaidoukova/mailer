from django.contrib import admin

from mailsender.models import Client, Mailing, MailingLogs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)
    search_fields = ('email', 'name',)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'stop_time', 'frequency', 'status', 'owner',)
    list_filter = ('status',)



@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'last_try', 'status',)

