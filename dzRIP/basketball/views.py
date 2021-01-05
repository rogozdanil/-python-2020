from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Commands


class CommandsView(View):
    def get(self, request):
        basketball = Commands.objects.all()
        return render(request, "basketball/basketball_list.html", {"basketball_list": basketball})


