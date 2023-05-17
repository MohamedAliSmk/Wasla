from djongo import models

class Merchant(models.Model):
    merchant_id = models.CharField(max_length=100)
    merchant_name = models.CharField(max_length=100)
    NameOfAccount_Manager = models.CharField(max_length=200)
    VPC_value = models.IntegerField()
    UIGmigs = models.IntegerField()
    Billing = models.IntegerField()
    CF_value = models.IntegerField()
    Salfny = models.IntegerField()
    Lending = models.IntegerField()
    TrxLastMonth  = models.IntegerField()
    TrxCurrentMonth  = models.IntegerField()
    VolumeLastMonth  = models.IntegerField()
    VolumeCurrentMonth  = models.IntegerField()
    ChurnType  = models.IntegerField()
    ChurnVolume  = models.IntegerField()
    ActiveTarget  = models.IntegerField()
    Current_MonthTarget   = models.CharField(max_length=20)
    Pre_MonthTarget   = models.CharField(max_length=20)

    def to_mongo(self):
        return {
            'merchant_id': self.merchant_id,
            'merchant_name': self.merchant_name,
            'NameOfAccount_Manager': self.NameOfAccount_Manager,
            'VPC_value': self.VPC_value,
            'UIGmigs': self.UIGmigs,
            'Billing': self.Billing,
            'CF_value': self.CF_value,
            'Salfny': self.Salfny,
            'Lending': self.Lending,
            'TrxLastMonth': self.TrxLastMonth,
            'TrxCurrentMonth': self.TrxCurrentMonth,
            'VolumeLastMonth': self.VolumeLastMonth,
            'VolumeCurrentMonth': self.VolumeCurrentMonth,
            'ChurnType': self.ChurnType,
            'ChurnVolume': self.ChurnVolume,
            'ActiveTarget': self.ActiveTarget,
            'Current_MonthTarget': self.Current_MonthTarget,
            'Pre_MonthTarget': self.Pre_MonthTarget,
        }