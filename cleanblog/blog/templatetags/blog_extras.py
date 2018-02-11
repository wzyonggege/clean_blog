from django import template
from cleanblog.blog.models import Post, Category, Tag

register = template.Library()

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def cate_list():
    return Category.objects.all()