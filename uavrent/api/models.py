from django.db import models

# Create your models here.

class UAVCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        #return the object as a full json
        obj = str(dict(self))
    #these are the basic fields for a UAV category model, we will hold the UAV information in another model and form a relationship between the two


class UAV(models.Model):
    name = models.CharField(max_length=100)
    _model = models.CharField(max_length=100)
    weight = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    category = models.ForeignKey(UAVCategory, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    #these are the basic fields for a UAV model, we will hold the rental information in another model and form a relationship between the two

class Rent(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    #renter will use the default user model
    renter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.uav.name + " rented by " + self.renter.username

    #this model will hold the rental information, we will form a relationship between the two models
