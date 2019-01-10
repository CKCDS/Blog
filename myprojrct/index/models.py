from django.db import models


# Create your models here.
class Category(models.Model):
    cate_name = models.CharField(max_length=50)

    def __repr__(self):
        return "<Category:%r>" % self.cate_name
    class Meta():
        db_table = "category"


class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __repr__(self):
        return "<Category:%r>" % self.type_name
    class Meta():
        db_table = "blogtype"


class User(models.Model):
    loginname = models.CharField(max_length=50)
    uname = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    upwd = models.CharField(max_length=30)
    is_author = models.IntegerField()
    class Meta():
        db_table = "user"

class Topic(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    read_num = models.IntegerField()
    content = models.TextField()
    images = models.TextField()
    blog_type = models.ForeignKey(BlogType)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User, related_name="topic")
    users = models.ManyToManyField(User, related_name="topics")
    class Meta():
        db_table = "topic"

class Reply(models.Model):
    content = models.TextField()
    reply_time = models.DateTimeField()
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    class Meta():
        db_table = "reply"