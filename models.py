from django.db import models

# Create your models here.


class Type_serializers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def GetChoces(cls):
        return [(type.id, type.name) for type in cls.objects.all()]

class Products_serializers(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to= 'media/pages/images/%y/%m/%d' )
    type = models.ForeignKey(Type_serializers, on_delete=models.CASCADE)
    

    def __str__(self):

        return self.name
    