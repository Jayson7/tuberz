from django.db import models

# Create your models here.


class video_url_keeper(models.Model):
    
    url = models.URLField()
    
    def __str__(self) -> str:
        return self.url