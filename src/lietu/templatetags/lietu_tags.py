from django import template
from ..models import DogGroup

register = template.Library()

@register.simple_tag
def get_dog_groups(num=8):
    return DogGroup.objects.all()[:num]
