from django.contrib import admin
from .models import Income, ExpenseCategory, Transaction

# Register your models here
admin.site.register(Income)
admin.site.register(ExpenseCategory)
admin.site.register(Transaction)
