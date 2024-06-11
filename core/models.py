from django.db import models

class CentralOffice(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} - {self.address}"

class Branch(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    central_office = models.ForeignKey(CentralOffice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city} - {self.address}"

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.account_number} - {self.client}"
