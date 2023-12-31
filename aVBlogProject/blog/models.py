# models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager




class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# post model
class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Taslak'),
    ('published', 'Yayında'),
    )

    title = models.CharField("Blog Başlığı", max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts', verbose_name='Yazar')
    body = RichTextUploadingField("İçerik")
    image = models.ImageField(upload_to='thumbnail/%Y/%m/%d/')
    tags = TaggableManager()
    
    publish = models.DateTimeField(default=timezone.now, verbose_name="Yayınlanma Tarihi")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField("Yayınlanma Durumu", max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        verbose_name_plural = "Blog Yazıları"
        verbose_name = "Yazı"
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
    
