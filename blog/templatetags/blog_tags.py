from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def cate_list():
    return Category.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)

