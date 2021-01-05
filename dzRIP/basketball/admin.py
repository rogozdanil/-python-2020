from django.contrib import admin
from .models import Player, Commands


admin.site.register(Commands)

admin.site.register(Player)
# Register your models here.
