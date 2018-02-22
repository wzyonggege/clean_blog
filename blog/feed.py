from django.contrib.syndication.views import Feed

from .models import Post

class AllPostRssFeed(Feed):
    title = "Clean Blog"

    link = "/"
    description = "My Blog"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{}] {}'.format(item.category, item.title)

    def item_description(self, item):
        return item.content