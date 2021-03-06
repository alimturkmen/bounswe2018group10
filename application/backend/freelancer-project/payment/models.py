from django.db import models

# Create your models here.

class Wallet(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    budget = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.id)


class Payment(models.Model):
    acceptedproject_id = models.ForeignKey('acceptedProject.AcceptedProject', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.id)
