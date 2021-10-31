from django.contrib import admin

# Register your models here.
from home.models import App, Plan, Subscription

class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'framework', 'description', 'user', 'created_at')

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'created_at')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan', 'app', 'user', 'active', 'created_at')


admin.site.register(App, AppAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
