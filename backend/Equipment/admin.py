from django.contrib import admin

# Register your models here.


from .models import Branch, User , Categories , subCategories , companyExperts , supportCompany , hardEquipment ,manufacturers


# Register your models here.


class branchAdmin(admin.ModelAdmin):
    list_display = ("branch_name", "branch_code")
    search_fields = ("branch_name", "branch_code")


class UserAdmin(admin.ModelAdmin):
    list_display = ("PersonalNo", "first_name", "last_name", "date_joined" ,"id")
    
    
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ("subCat_name","subCat_subset" ,"subCat_model")

class ExpertsAdmin(admin.ModelAdmin):
    list_display = ("expertFistName" , "expertLastName" , "expertMobile" , "expertcompany")
    

class CompanyAdmin(admin.ModelAdmin):
    list_dispaly = ("companyName","companyPhoneMobile")





admin.site.register(User, UserAdmin)
admin.site.register(Branch, branchAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(subCategories,SubCategoriesAdmin)
admin.site.register(companyExperts , ExpertsAdmin)
admin.site.register(supportCompany , CompanyAdmin)
admin.site.register(manufacturers)
admin.site.register(hardEquipment)
