import graphene
from Equipment import models
from Equipment import types
from graphene_django import DjangoListField

class Query(graphene.ObjectType):
    user = graphene.Field(types.UserType)
    
    all_branches = graphene.List(types.BranchType)
    branches_by_code = graphene.List(types.BranchType, branch_code=graphene.Int())
    branches_by_name = graphene.List(types.BranchType, branch_name=graphene.String())

    all_supportCompany = graphene.List(types.supportCompanyType)
    supportCompany_by_name = graphene.List(types.supportCompanyType , companyName = graphene.String())
    
    all_categories = graphene.List(types.CategoryType)
    all_subCategories = graphene.List(types.SubCategoryType)
    subCategories_by_categories = graphene.List( types.SubCategoryType , subCat_subset = graphene.String())
    subCategories_by_supportCo = graphene.List(types.SubCategoryType , subCat_SupportCo = graphene.String())
    
    all_companyExperts = graphene.List(types.companyExpertsType)
    companyExperts_by_company = graphene.List(types.companyExpertsType , expertcompany = graphene.String())

    all_manufactuers = graphene.List(types.manufacturersType)

    def resolve_all_manufactuers(root , info):
        return(
            models.manufacturers.objects.all()
        )
    
    def resolve_all_supportCompany(root , info ):
        return (
            models.supportCompany.objects.all()
        )
        
    
    def resolve_supportCompany_by_name(root , info , companyName ):
        return (
            models.supportCompany.objects.filter(companyName = companyName)
        )

        
    def resolve_companyExperts_by_company(root , info , expertcompany ):
        return (
            models.companyExperts.objects.filter( expertcompany__companyName = expertcompany)
        )

    def resolve_all_companyExperts(root , info ):
        return (
            models.companyExperts.objects.all().order_by("expertcompany")
        )

    def resolve_all_subCategories_by_supportCo(root , info , supportCo ):
        return (
            models.subCategories.objects.filter( subCat_SupportCo = supportCo)
        )


    
    def resolve_all_subCategories(root , info):
        return (
            
            models.subCategories.objects.all()
        )
        
    
    
    def resolve_all_categories(root , info):
        return (
            models.Categories.objects.all()
        )
    
    
    def resolve_user(root, info):
        return (
            models.User.objects.first()
        )

    def resolve_all_branches(root, info):
        return (
            models.Branch.objects.all().order_by("branch_code")
        )

    def resolve_branches_by_code(root, info , branch_code):
        return (
            models.Branch.objects.filter(branch_code = branch_code)
        )
        
    def resolve_branches_by_name(root, info , branch_name):
        return (
            models.Branch.objects.filter(branch_name=branch_name)
        )