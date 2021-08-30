from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    def _str_(self):
        return self.category
