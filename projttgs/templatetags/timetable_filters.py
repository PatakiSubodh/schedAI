from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(meeting_times, day_id):
    return meeting_times.filter(pid=day_id).first()
