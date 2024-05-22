from django.db import models

# Create your models here.

class AccountList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CityList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ContractDuration(models.Model):
    duration = models.CharField(max_length=50)

    def __str__(self):
        return str(self.duration)

class Month(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Distributor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class GraphList(models.Model):
    margin = models.IntegerField()
    win_probability = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.win_probability)
    

class Tender(models.Model):
    tender_name = models.CharField(max_length=255,unique=True)
    quantity = models.IntegerField()
    price_a = models.DecimalField(max_digits=10, decimal_places=2)
    account_list = models.ForeignKey(AccountList, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    city_list = models.ForeignKey(CityList, on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
    contract_duration = models.ForeignKey(ContractDuration, on_delete=models.CASCADE,null=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE,null=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE,null=True)
    graph_list = models.ForeignKey(GraphList,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.tender_name
    

class TenderB(models.Model):
    tender_name = models.CharField(max_length=255,unique=True)
    quantity = models.IntegerField()
    price_b = models.DecimalField(max_digits=10, decimal_places=2)
    account_list = models.ForeignKey(AccountList, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    city_list = models.ForeignKey(CityList, on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
    contract_duration = models.ForeignKey(ContractDuration, on_delete=models.CASCADE,null=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE,null=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE,null=True)
    graph_list = models.ForeignKey(GraphList,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.tender_name


    



