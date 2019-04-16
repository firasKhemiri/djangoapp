from django.contrib import admin
from push_notifications.models import GCMDevice

from customUser.models import User, PostStat, Commentaire, Message, Conversation, Category, Event, Notification, \
    Suggest, Courses, Department, Schedule, Pending, Classe, Branch


class CategoryAdmin(admin.ModelAdmin):

    search_fields = ('name', 'description', 'id',)


admin.site.register(User)
admin.site.register(Category,CategoryAdmin)
admin.site.register(PostStat)
admin.site.register(Event)
admin.site.register(Commentaire)
admin.site.register(Message)
admin.site.register(Conversation)
admin.site.register(Notification)
admin.site.register(Suggest)

admin.site.register(Courses)
admin.site.register(Department)
admin.site.register(Schedule)

admin.site.register(Classe)
admin.site.register(Branch)

admin.site.register(Pending)


