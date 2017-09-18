from django import template

register = template.Library()


@register.filter(name='has_player_group')
def has_player_group(user):
    return user.groups.filter(name='Player').exists()


@register.filter(name='has_administrator_group')
def has_administrador_group(user):
    return user.groups.filter(name='Administrator').exists()
