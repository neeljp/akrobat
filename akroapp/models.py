from django.db import models

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    creater = models.ForeignKey('auth.User', related_name='exercises', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=250)
    tags = models.ManyToManyField('Tag',related_name='+',blank=False)
    videourl = models.URLField(max_length=200, default='')
    pictureurl = models.URLField(default='', max_length=200)

    class Meta:
        ordering = ('created',)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
