from django.contrib import admin

from mailings.models import Mailing, Client, MailingLog


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'sending_time_start', 'sending_time_end', 'periodicity', 'status',
                    'mail_title', 'pk', ]
    list_filter = ['periodicity', 'status', 'owner']
    search_fields = ['title', 'description', 'mail_title', 'mail_content']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mailing', ]
    list_filter = ['mailing', ]


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MailingLog._meta.get_fields()]
    list_filter = ['status', 'mailing_date']
