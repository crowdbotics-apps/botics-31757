from django.contrib import admin

# Register your models here.
from home.models import App, Plan

class AppAddmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'framework', 'description', 'user', 'created_at')

class PlanAddmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'created_at')


admin.site.register(App, AppAddmin)
admin.site.register(Plan, PlanAddmin)

