from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    PersonalNo = models.CharField( max_length=8 ,null=True)
    location = models.CharField(max_length=30, null=True)
    joined_date = models.DateField(auto_now_add=True)
    national_code = models.BigIntegerField(null=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = '2. کاربران'

    def __str__(self):
        return self.last_name


class Branch(models.Model):
    branch_code = models.IntegerField(unique=True)
    branch_name = models.CharField(max_length=30)
    branch_dgree = models.CharField(max_length=20)
    branch_person_no = models.IntegerField()
    
    class Meta:
        verbose_name = 'شعبه'
        verbose_name_plural = '1. شعب'

    def __str__(self):
        return self.branch_name

class Categories(models.Model):
    
    category_name = models.CharField(max_length= 150 , unique= True) 
    create_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'انوع سخت افزار'
        verbose_name_plural = '3. انواع سخت افزار'
        
    def __str__(self):
        return self.category_name
    
    
class subCategories(models.Model):
    
    subCat_subset = models.ForeignKey("Categories" , on_delete= models.CASCADE)
    subCat_name = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now=True)
    subCat_model = models.CharField(max_length=50 , blank=True)
    subCat_SupportCo = models.ForeignKey("supportCompany",  on_delete=models.CASCADE , null=True)
    subCat_manufacture = models.ForeignKey("manufacturers" , on_delete=models.CASCADE , null=True)
    
    class Meta:
        verbose_name = 'دسته بندی ها'
        verbose_name_plural = '4.  دسته بندی'
    
    def __str__(self):
        return f'{self.subCat_name} - {self.subCat_subset} - {self.subCat_model}'
    

class companyExperts(models.Model):
    expertFistName = models.CharField(max_length= 100)
    expertLastName = models.CharField(max_length=150)
    expertMobile = models.CharField(max_length=13 , unique=True)
    expertcompany = models.ForeignKey("supportCompany" , on_delete= models.CASCADE)
    
    class Meta:
        verbose_name = 'کارشناسان'
        verbose_name_plural = '5. کارشناسان شرکت ها'
        
    def __str__(self):
        return self.expertLastName
    

class supportCompany(models.Model):
    companyName = models.CharField(max_length=100)
    companyCEOName = models.CharField(max_length=100  , blank=True )
    companyPhon1 = models.CharField( max_length=13)
    companyPhon2 = models.CharField( max_length=13 , blank=True)
    companyPhon3 = models.CharField( max_length=13 , blank=True)
    companyRank = models.CharField(max_length= 50 , blank=True)
    companyPhoneMobile = models.CharField( max_length=13 , blank=True)
    
    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = '6.  شرکت پشتیبان'
        
    def __str__(self):
        return self.companyName
    

class manufacturers(models.Model):
    manufName = models.CharField(max_length=100 , unique=True)
    manufAgency = models.CharField(max_length=100 , blank= True)
    
    class Meta:
        verbose_name = 'سازنده محصول'
        verbose_name_plural = '7. کارخانه سازنده محصول'
        
    def __str__(self):
        return self.manufName
    


    

class hardEquipment(models.Model):
    hardName = models.ForeignKey("subCategories", on_delete=models.CASCADE)
    hardAssetNumber = models.IntegerField()
    hardModel = models.CharField(max_length=50)
    hardManufacturer = models.ForeignKey("manufacturers",  on_delete=models.CASCADE)
    hardSerial = models.CharField(max_length=50)
    hardFanavariNumber = models.IntegerField()
    hardDesciption = models.CharField(max_length=300 , blank=True)
    hardSize = models.CharField(max_length= 50)
    hardBranch = models.ForeignKey("Branch",  on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'سخت افزار'
        verbose_name_plural = '8. سخت افزار'
        
    def __str__(self):
        return f'{self.hardName} - سریال {self.hardSerial} -  اموال {self.hardAssetNumber}'
    
    
    
    
    
        