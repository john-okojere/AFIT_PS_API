from django.db import models

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    amount = models.DecimalField(verbose_name= "AMOUNT (ETH)",max_digits=18, decimal_places=18)
    amount_ngn = models.IntegerField( verbose_name="AMOUNT (NGN)")
    timestamp = models.DateTimeField(auto_now_add=True)
    matric = models.CharField(max_length=50)
    gmail = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment from {self.sender} to {self.receiver} - {self.amount} ETH"


class Admin(models.Model):
    wallet_address = models.CharField(max_length=42)



class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Level(models.Model):
    department = models.ForeignKey(Department, related_name='levels', on_delete=models.CASCADE)
    level = models.IntegerField()
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.department.name} - Level {self.level}"