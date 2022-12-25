from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    pub_date = models.DateTimeField('date published')
    slug=models.SlugField()
    parent=models.ForeignKey('self',blank=True,null=True, related_name='children',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    category=models.ForeignKey(Category, on_delete=models.CASCADE) #category tablosu ile ilişkilendirme
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    file = models.FileField(blank=True, upload_to='files/')
    status = models.CharField(max_length=10, choices=STATUS)
    pub_date = models.DateTimeField('date published')
    slug=models.SlugField()

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Images(models.Model):
    content=models.ForeignKey(Content,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title