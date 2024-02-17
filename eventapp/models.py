from django.db import models

# Create your models here.
class Decoration(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    amount=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Catering(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)


    def __str__(self):
        return self.name



class Photoshoot(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    amount=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Booking(models.Model):
    cus_name = models.CharField(max_length=55)
    cus_ph = models.CharField(max_length=10)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE)
    catering = models.ForeignKey(Catering, on_delete=models.CASCADE)
    photoshoot = models.ForeignKey(Photoshoot, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
