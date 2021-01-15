from django.shortcuts import render
from basketball.models import Player, Commands
from django.template.defaulttags import register


@register.filter
def next(list, index):
    try:
        return list[index + 1]
    except:
        return ' '


def index(request):
    command_list = Commands.objects.all()
    return render(request, 'basketball/basketball_list.html', {
        'command_list': command_list
    })


def commands(request):
    command_list = Commands.objects.all()
    return render(request, 'basketball/command_list.html', {
        'command_list': command_list
    })


def one_command(request, pk):
    command = Commands.objects.get(pk=pk)
    return render(request, 'basketball/command.html', {
        'command': command
    })


def players(request):
    player_list = Player.objects.all()
    return render(request, 'basketball/player_list.html', {
        'player_list': player_list
    })


def one_player(request, pk):
    player = Player.objects.get(pk=pk)
    return render(request, 'basketball/player.html', {
        'player': player
    })
