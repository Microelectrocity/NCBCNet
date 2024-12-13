from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from mptt.models import MPTTModel,TreeForeignKey
from ckeditor.fields import RichTextField
# Create your models here.

class Comment(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    reply_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='replyers')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('created',)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.content[:20]