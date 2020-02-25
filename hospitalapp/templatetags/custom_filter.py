from django import template
from hospitalapp.models import Menu

register = template.Library()


@register.filter
def getChilds(parentId):
    return Menu.objects.filter(id_parent=parentId)

@register.filter
def hasChilds(parentId):
    childs =  Menu.objects.filter(id_parent=parentId)
    if(childs is not None):
        if(len(childs) > 0):
            return "True"
    return "False"


