from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    likes = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def likes_on_post(self):
        return Like.objects.filter(likes=self).count()

    def comment_on_post(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user','post',)


class Like(models.Model):
    likes = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('likes','post',)


