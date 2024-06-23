from django.contrib import admin
from .models import CoachModel , PlayersModel
# Register your models here.
admin.site.register(CoachModel)
admin.site.register(PlayersModel)