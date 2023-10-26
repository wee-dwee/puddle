from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name
    
class items(models.Model):
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    desc=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name_plural='items'

    def __str__(self) -> str:
        return self.name