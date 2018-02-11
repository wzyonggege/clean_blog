import xadmin
from xadmin import views

from .models import Post, Category, Tag

class GlobalSetting(object):
    site_title = 'clean blog v.1.0'
    site_footer = 'my blog'

xadmin.site.register(views.CommAdminView, GlobalSetting)

#注册到后台
xadmin.site.register(Post)
xadmin.site.register(Category)
xadmin.site.register(Tag)

