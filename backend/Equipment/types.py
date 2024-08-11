import graphene
from graphene_django import DjangoObjectType
from Equipment import models


class BranchType(DjangoObjectType):
    class Meta:
        model = models.Branch


class UserType(DjangoObjectType):
    class Meta:
        model = models.User

class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Categories

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = models.subCategories
        
class companyExpertsType(DjangoObjectType):
    class Meta:
        model = models.companyExperts
        
class supportCompanyType(DjangoObjectType):
    class Meta:
        model = models.supportCompany
        
class manufacturersType(DjangoObjectType):
    class Meta:
        model = models.manufacturers
        
class hardEquipmentType(DjangoObjectType):
    class Meta:
        model = models.hardEquipment
