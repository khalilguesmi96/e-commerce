from django.db import models
from django.conf import settings
# Create your models here.
CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW','Sport Wear'),
    ('OW','Outwear'),
('PH','Phone'),
('PC','Pc'),

)
LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),

)



class Item(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    image = models.ImageField(null=True,blank=True,upload_to='images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


    def __str__(self):
        return self.title

class Order(models.Model):
    use = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.use.username