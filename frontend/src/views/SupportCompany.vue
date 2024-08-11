<template>
    <div>
      <!-- <menu-section /> -->
   
      
      
  
      <!-- <div class="nav-logo text-2xl text-xl font-semibold " >
        <h1 v-for="br_name in mySite">{{ br_name.branchName  }} - {{ br_name.branchCode  }}</h1>
              
            </div> -->
            
<div>
  <h3 class="font-bold mt-10 text-center mb-5">فهرست شرکت های پشتیبان </h3>
</div>


<div  class="relative w-full overflow-x-auto shadow-md sm:rounded-lg">

    <div v-if="showNewExpert" class="mt-5">
  <form  @submit.prevent="NewExpert" class=" max-w-md mx-auto ">
  
  <div class=" w-full grid md:grid-cols-2 md:gap-6">
    <div class="relative z-0 w-full mb-5 group">
        <input  v-model="expertFirstName"
        type="text" name="floating_first_name" id="floating_first_name" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام  </label>
    </div>
    <div class="relative z-0 w-full mb-5 group">
        <input  v-model="expertLastName"
        type="text" name="floating_last_name" id="floating_last_name" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_last_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام خانوادگی </label>
    </div>
  


    <div class="relative z-0 w-full mb-5 group">
        <input v-model="expertMobile"
        type="number"  name="dgree" id="floating_phone" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_phone" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">شماره  موبایل</label>
    </div>

  
  
  <div class="relative z-0 w-full mb-5 group">
<select  class="dropdown rounded-lg w-full"  v-model="expertCompanySelected" @change="getExpertCompanyID">
<option  value="">نام شرکت</option>
<option v-for="company in companies" :key="company.companyName" 
      :value="company.companyName">{{company.companyName}}</option>
</select>

</div>
</div>

  
  <button type="submit" class=" text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> ثبت </button>
</form>
</div>

  <div v-if="showNewCompany" class="mt-5">
  <form  @submit.prevent="NewCompany" class=" max-w-md mx-auto ">
  
  <div class=" w-full grid md:grid-cols-2 md:gap-6">
    <div class="relative z-0 w-full mb-5 group">
        <input v-model="companyName"
        type="text" name="floating_first_name" id="floating_first_name" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام شرکت    </label>
    </div>
    <div class="relative z-0 w-full mb-5 group">
        <input  v-model="companyCEOName"
        type="text" name="floating_last_name" id="floating_last_name" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_last_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام مدیرعامل </label>
    </div>
  </div>
  <div class="grid md:grid-cols-2 md:gap-6">
    <div class="relative z-0 w-full mb-5 group">
        <input v-model="companyPhon1"
        type="number"  name="dgree" id="floating_phone" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_phone" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">شماره تلفن شرکت</label>
    </div>
    <div class="relative z-0 w-full mb-5 group">
        <input  v-model="companyPhoneMobile"
         type="number" name="floating_company" id="floating_company" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" required />
        <label for="floating_company" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"> شماره موبایل مدیرعامل</label>
    </div>
  </div>
  <button type="submit" class=" text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> ثبت </button>
</form>
</div>
    <table class=" w-full  text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">
            <tr >
                <th scope="col" class="px-6 py-3">
                    نام  </th>
                <th scope="col" class="px-6 py-3">
                          نام خانوادگی  </th>   
                <th scope="col" class="px-6 py-3">
                     شماره موبایل    
                </th>
                <th scope="col" class="px-6 py-3">

                    <select  class="dropdown rounded-lg w-full"  v-model="selectedCompany" @change="CurrentCompany">
       <option  value="">نام شرکت</option>
       <option v-for="company in companies" :key="company.companyName" 
                          :value="company.companyName">{{company.companyName}}</option>
  </select>


                </th>


                <th scope="col" class="px-6 py-3">
                    شماره تلفن شرکت
                </th>
                
                <th scope="col" class="px-6 py-3">
                    <button 
            @click="newCompanyDefin"      class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
    شرکت جدید 
  </button>
                </th>
                <th scope="col" class="flex px-6 py-3">
                  
                  <!-- <a href="/newbranch" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">شعبه جدید</a> -->
                   
                 
  <button 
            @click="newExpertDefin"      class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
    پشتیبان جدید
  </button>

                
                </th>
            </tr>
        </thead>
        
        <tbody>
      


  <tr    v-for=" expert in allExperts " :key="expert" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-orange-200 dark:hover:bg-gray-600">
      <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ expert.expertFistName   }}
      </th>
      <td class="px-6 py-4">
          {{ expert.expertLastName}}
      </td>
      <td class="px-6 py-4">
          {{ expert.expertMobile}}
      </td>
      <td class="px-6 py-4">
          {{ expert.expertcompany.companyName}}
      </td>

      <td class="px-6 py-4">
          {{ expert.expertcompany.companyPhon1}}
      </td>
      
      
      <td class="px-6 py-4 text-right">
          <!-- <a  href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">ویرایش</a> -->
          <button  @click.prevent="updateExpertDefine(expert.expertFistName , expert.expertLastName , expert.expertMobile , expert.expertcompany.companyName)" 
                        class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" >
          ویرایش 
          
        </button>
      </td>
      <td class="px-6 py-4 text-right">
          <!-- <a  href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">ویرایش</a> -->
          <button  @click.prevent="delExpert(expert.expertMobile)" 
                        class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" >
          حذف 
          
        </button>
      </td>

  </tr>

            
        </tbody>

    </table>
    
</div>

    </div>
  
    
</template>

<script>
import { AllExpertName , CompanyByName , supportsCo , supportCoByName}  from "../queries";
import { useUserStore } from "@/user/user";
import { New_Company , New_Expert , Delete_Expert } from '@/mutaions';

export default {
    name : "SupportCompany" ,

    data(){
        return{
            loginUser: useUserStore(),

            companies : null,
            showNewCompany : false ,
            showNewExpert : false ,
            allExperts : null ,
            selectedCoData : null,
            selectedCompany : "" ,


            companyName: "", 
            companyPhon1: 0,
            companyPhon2: 0,
            companyPhon3: 0,
            companyPhoneMobile : 0,
            companyRank: 0,
            companyCEOName : "",

            expertFirstName : "",
            expertLastName : "",
            expertMobile : 0,
            expertcompanyID : 0,

            expertCompanySelected : "",





            
            
        }
    },

    async created() {


            const siteInfo = await this.$apollo.query({
              query: AllExpertName,
            });
            this.allExperts = siteInfo.data.allCompanyexperts;
        
        

      const supportCompany = await this.$apollo.query({
        query: supportsCo,
      });
      this.companies= supportCompany.data.allSupportcompany

      ;
      
      
    },

    methods:{

        async  delExpert(expertMobile){
      if(this.loginUser.token ){
        
        if (window.confirm(" آیا از حذف پشتیبان مطمئن هستید")){

          const deleteInfo = await this.$apollo.mutate({
            mutation: Delete_Expert,
            variables: {
    
              expertMobile : expertMobile ,
            }
          });
                  location.reload();
        }
        }else{
        alert("شما وارد سیستم نشده اید")
        }
      
    },

    
    async  updateExpertDefine(expertFirstName , expertLastName , expertMobile  ){
      if(this.loginUser.token ){
        this.showNewExpert = !this.showNewExpert
                this.showNewCompany = false

        }else{
        alert("شما وارد سیستم نشده اید")
        }

        this.expertFirstName = expertFirstName
        this.expertLastName = expertLastName
        this.expertMobile = expertMobile
        
      
    },



        async getExpertCompanyID(){
            const company = await this.$apollo.query({
                query: supportCoByName ,
                variables:{
                    companyName : this.expertCompanySelected
                    
                }

            });

                this.expertcompanyID = company.data.supportCompanyByName[0].id                
        },
        

        async NewExpert() {

            
        const newExpert1 = await this.$apollo.mutate({

          mutation: New_Expert ,
          
                  
                  
            variables: {

                expertFistName  :  this.expertFirstName , 
                expertLastName :  this.expertLastName ,
                expertMobile :  this.expertMobile ,
                expertcompany : this.expertcompanyID

            },
        });
        
        this.expertFirstName = ""
        this.expertLastName = ""
        this.expertMobile = 0
        location.reload();

      
    },

        
    async NewCompany() {
        
        const newComapny1 = await this.$apollo.mutate({

          mutation: New_Company ,
          
                  
                  
            variables: {

              companyName  :  this.companyName , 
              companyPhon1 :  this.companyPhon1 ,
              companyPhon2 :  this.companyPhon2 ,
              companyPhon3 :  this.companyPhon3 ,
              companyPhoneMobile :   this.companyPhoneMobile ,
              companyRank :  this.companyRank ,
              companyCEOName  :  this.companyCEOName  ,

            },
        });
        
        location.reload();

      
    },
        async  newCompanyDefin() {
            
      if(this.loginUser.token ){

          this.showNewCompany = !this.showNewCompany
          this.showNewExpert = false
        }else{
          this.showNewCompany = false
          alert("شما وارد سیستم نشده اید")
      }
    //   this.mutateBranch = NEW_BRANCH

    },

    async  newExpertDefin() {
            
            if(this.loginUser.token ){
      
                this.showNewExpert = !this.showNewExpert
                this.showNewCompany = false
              }else{
                this.showNewExpert = false
                alert("شما وارد سیستم نشده اید")
            }
          //   this.mutateBranch = NEW_BRANCH
      
          },
      
      

        // async selectedCompany(){
        //     // this.isSelectCo = co
        //     console.log("test")
        // },


        async CurrentCompany(){
            
            const company = await this.$apollo.query({
                query: CompanyByName ,
                variables:{
                    expertcompany : this.selectedCompany
                    
                }
                
            });
            
            if( this.selectedCompany != ""){

                this.allExperts = company.data.companyExpertsByCompany
            } else {
                location.reload();
            }
                        
        }
    }

}
</script>