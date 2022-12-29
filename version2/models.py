from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.

from users.models import User

class Services(models.Model):
    name = models.CharField(max_length=100)
    Description = models.CharField(max_length=250)
    Logo = models.CharField(max_length=250)

    class Meta:
        db_table = "services"
    
    def __str__(self):
        return self.name    



class Payment_user(models.Model):
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='userss')
    servicio = models.ForeignKey(Services,on_delete =models.CASCADE, related_name='services')
    Amount = models.FloatField(default=0.0)
    PaymentDate = models.DateField(auto_now_add=True)
    ExpirationDate = models.DateField()

    def __str__(self):
        return str(self.pk)



class Expired_payments(models.Model):
    Payment_user_id = models.ForeignKey(Payment_user,on_delete =models.CASCADE, related_name='services')
    Penalty_fee_amount = models.FloatField(default=0.0)
    