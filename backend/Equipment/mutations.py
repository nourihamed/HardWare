import graphene
from Equipment import models ,  types
import graphql_jwt


##########  categories

class NewCategory(graphene.Mutation):
    NewCat = graphene.Field(types.CategoryType)
    
    class Arguments:
        categoryName = graphene.String(required = True)
        
    def mutate(self , info , categoryName ):
        NewCat = models.Categories(
            category_name = categoryName
        )
        
        NewCat.save()
        
        return NewCategory(NewCat)
    
    
    
class DeleteCategory(graphene.Mutation):
    delCat = graphene.Field(types.CategoryType)
    class Arguments:
        categoryName = graphene.String(required = True)
    
    def mutate(self , info , categoryName ):
        delCat = models.Categories.objects.get(category_name = categoryName)
        delCat.delete()
        
        return DeleteCategory(delCat)
    
    

class CreateNewManufacture(graphene.Mutation):
    newManufacture = graphene.Field(types.manufacturersType)
    
    class Arguments:
        manufName = graphene.String(required = True)
        manufAgency = graphene.String()
        
    def mutate(self , info , manufName , manufAgency ):
        newManufacture = models.manufacturers(
            manufName = manufName ,
            manufAgency = manufAgency
               
        )
        
        newManufacture.save()
        
        return CreateNewBranch(newManufacture)

class DeleteManufacture(graphene.Mutation):
    delManuf = graphene.Field(types.manufacturersType)
    
    class Arguments:
        manufName =graphene.String()
        
    def mutate(self , info , manufName):
        delManuf = models.manufacturers.objects.get(manufName = manufName)
        delManuf.delete()
        return DeleteManufacture(manufName)
        

##########  experts

class DeleteExpert(graphene.Mutation):
    delExpert =  graphene.Field(types.companyExpertsType)
        
    class Arguments:
        expertMobile = graphene.BigInt()


    def mutate(self , info   , expertMobile):
        
        delExpert = models.companyExperts.objects.get(expertMobile=expertMobile)
        delExpert.delete()
        return DeleteExpert(delExpert)
 

class UpdateExpert(graphene.Mutation):
    upExpert =  graphene.Field(types.companyExpertsType)
        
    class Arguments:
        expertFistName = graphene.String(required = True)
        expertLastName = graphene.String(required = True)
        expertMobile = graphene.BigInt()
        expertcompany = graphene.ID()

    def mutate(self , info , expertFistName , expertLastName , expertMobile , expertcompany):
        
        delExpert = models.companyExperts.objects.get(expertMobile=expertMobile)
        
        company = models.supportCompany.objects.get(pk=expertcompany)
        
        NewExpert = models.companyExperts(
        expertFistName = expertFistName ,
        expertLastName = expertLastName ,
        expertMobile = expertMobile ,
        expertcompany = company,

        )
        
        delExpert.delete()
        NewExpert.save()
        
        return UpdateExpert(NewExpert)
 

class CreateNewExpert(graphene.Mutation):
    newExpert =  graphene.Field(types.companyExpertsType)
        
    class Arguments:
        expertFistName = graphene.String(required = True)
        expertLastName = graphene.String(required = True)
        expertMobile = graphene.BigInt()
        expertcompany = graphene.ID()

    def mutate(self , info , expertFistName , expertLastName , expertMobile , expertcompany):
        
        company = models.supportCompany.objects.get(pk=expertcompany)
        
        newExpert = models.companyExperts(
        expertFistName = expertFistName ,
        expertLastName = expertLastName ,
        expertMobile = expertMobile ,
        expertcompany = company,

        )
        
        newExpert.save()
        
        return CreateNewExpert(newExpert)
        

class CreateNewSupportCompany(graphene.Mutation):
    newCompany =  graphene.Field(types.supportCompanyType)
        
    class Arguments:
        companyName = graphene.String(required = True)
        companyPhon1 = graphene.BigInt()
        companyPhon2 = graphene.BigInt()
        companyPhon3 = graphene.BigInt()
        companyRank = graphene.Int()
        companyPhoneMobile = graphene.BigInt()
        companyCEOName = graphene.String()
        
    def mutate(self , info , companyName ,companyCEOName ,companyPhon1 , companyPhon2 , companyPhon3 , companyRank , companyPhoneMobile):
        
        newCompany = models.supportCompany(
        companyName = companyName ,
        companyPhon1 = companyPhon1 ,
        companyPhon2 = companyPhon2 ,
        companyPhon3 = companyPhon3 ,
        companyRank = companyRank ,
        companyPhoneMobile = companyPhoneMobile,
        companyCEOName = companyCEOName
        )
        
        newCompany.save()
        
        return CreateNewSupportCompany(newCompany)
        

class DeleteCompany(graphene.Mutation):
    delCompany = graphene.Field(types.supportCompanyType)
    
    class Arguments:
        company_Name = graphene.String(required = True)
    
    def mutate(self , info , company_Name):
        delCompany = models.supportCompany.objects.get(companyName = company_Name)
        delCompany.delete()
        
        return DeleteBranch(delCompany)      
        
        
 ####### branches #############       

########  branches

class UpdateBranch(graphene.Mutation):
    upBranch = graphene.Field(types.BranchType)
    
    class Arguments:
        branch_code = graphene.Int(required = True)
        branch_name = graphene.String(required = True)
        branch_dgree = graphene.String()
        branch_person_no = graphene.Int(required = True)
        
    def mutate(self , info , branch_code , branch_name , branch_dgree , branch_person_no):
        
     
        delBranch = models.Branch.objects.get(branch_code= branch_code)
        
        newBranch = models.Branch(
            branch_code = branch_code,
            branch_name = branch_name,
            branch_dgree = branch_dgree,
            branch_person_no = branch_person_no
    
        )

        delBranch.delete()
        newBranch.save()
        
        return UpdateBranch(newBranch)
    
    
class DeleteBranch(graphene.Mutation):
    delBranch = graphene.Field(types.BranchType)
    
    class Arguments:
        branch_code = graphene.Int(required = True)
    
    def mutate(self , info , branch_code):
        delBranch = models.Branch.objects.get(branch_code= branch_code)
        delBranch.delete()
        
        return DeleteBranch(delBranch)       
    

class CreateNewBranch(graphene.Mutation):
    newBranch = graphene.Field(types.BranchType)
    
    class Arguments:
        branch_code = graphene.Int(required = True)
        branch_name = graphene.String(required = True)
        branch_dgree = graphene.String()
        branch_person_no = graphene.Int(required = True)
        
    def mutate(self , info , branch_code , branch_name , branch_dgree , branch_person_no):
        newBranch = models.Branch(
            branch_code = branch_code,
            branch_name = branch_name,
            branch_dgree = branch_dgree,
            branch_person_no = branch_person_no
    
        )
        
        newBranch.save()
        
        return CreateNewBranch(newBranch)

############## users ################

class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)
    
    class Arguments:
        username = graphene.String(required = True)
        password = graphene.String(required = True)
        PersonalNo = graphene.String(required = True)
      
    
    def mutate(self , info , username , password , PersonalNo ):
        user = models.User(
            username = username ,
            PersonalNo = PersonalNo ,
            
        )
    
        user.set_password(password)
        user.save()
        
        return CreateUser(user = user)
    
## costumized token
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)
    

class Mutation(graphene.ObjectType):
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    token_auth = ObtainJSONWebToken.Field()
    
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    createUser = CreateUser.Field()
    CreateNewBranch = CreateNewBranch.Field()
    DeleteBranch = DeleteBranch.Field()
    UpdateBranch = UpdateBranch.Field()
    createNewCompany = CreateNewSupportCompany.Field()
    deleteCompany = DeleteCompany.Field()
    CreateNewExpert  = CreateNewExpert.Field()
    UpdateExpert = UpdateExpert.Field()
    DeleteExpert = DeleteExpert.Field()
    CreateNewManufacture = CreateNewManufacture.Field()
    DeleteManufacture =  DeleteManufacture.Field()
    NewCategory = NewCategory.Field()
    DeleteCategory = DeleteCategory.Field()
    