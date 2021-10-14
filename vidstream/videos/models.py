from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class PublishStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'
    #UNLISTED='UN','Unlisted'
    #Private='PR','Private'
    
    

class VideoQuerySet(models.QuerySet):
    def published(self):
        now=timezone.now()
        return self.filter(state=Video.VideoStateOptions.PUBLISH,publish_timestamp_lte=now)
    
 
class VideoManager(models.Manager):
    def get_queryset(self):
            return VideoQuerySet(self.model,using=self._db)
        
    def published(self):
        return self.get_queryset()




class Video(models.Model):
    
    VideoStateOptions=PublishStateOptions
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    slug=models.SlugField(blank=True,null=True)
    video_id = models.CharField(max_length=200,unique=True)
    active=models.BooleanField(default=True)
    state=models.CharField(max_length=2,choices=VideoStateOptions.choices,default=VideoStateOptions.DRAFT)
    publish_timestamp=models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    objects=VideoManager()
    
    @property
    def is_published(self):
        return self.active
    
    def save(self,*args,**kwargs):
        
        if self.slug is None:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
        
    
class VideoPublishedProxy(Video):
    class Meta:
        proxy=True
        verbose_name="Published Video"
        verbose_name_plural="Published Videos"
        

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "All Video"
        verbose_name_plural = "All Videos"
        
def publish_state_pre_save(sender,instance,*args,**kwargs):
    if instance.state == PublishStateOptions.PUBLISH and instance.publish_timestamp is None:

            print("save is published")
            self.publish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.publish_timestamp=None
        
