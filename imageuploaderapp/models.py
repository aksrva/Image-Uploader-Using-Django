from django.db import models

# Create your models here.


class ImageUploader(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image}"
