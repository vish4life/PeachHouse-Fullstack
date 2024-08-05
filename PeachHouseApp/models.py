from django.db import models

# Create your models here.
class Menu(models.Model):
    # id = models.SmallIntegerField(primary_key=True,db_index=True)
    title=models.CharField(max_length=255,db_index=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    inventory=models.SmallIntegerField()
    def __str__(self) :
        return self.title

class Booking(models.Model):
    id=models.SmallIntegerField(primary_key=True,db_index=True)
    name=models.CharField(max_length=255,null=False)
    no_of_guests=models.SmallIntegerField()
    booking_date=models.DateTimeField()


