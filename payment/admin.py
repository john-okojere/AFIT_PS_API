from django.contrib import admin
from .models import Admin, Payment

class AdminAdmin(admin.ModelAdmin):
    list_display = ('wallet_address',)
    search_fields = ('wallet_address',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('gmail', 'matric', 'amount', 'status')  # Ensure these fields are valid
    search_fields = ('gmail', 'matric')
    list_filter = ('status',)

admin.site.register(Admin, AdminAdmin)
admin.site.register(Payment, PaymentAdmin)

from django.contrib import admin
from .models import Department, Level

class LevelInline(admin.TabularInline):
    model = Level
    extra = 1

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [LevelInline]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Level)
