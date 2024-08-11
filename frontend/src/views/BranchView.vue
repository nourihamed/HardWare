
<template>
    <div>
      <!-- <menu-section /> -->
   
      
      
  
      <!-- <div class="nav-logo text-2xl text-xl font-semibold " >
        <h1 v-for="br_name in mySite">{{ br_name.branchName  }} - {{ br_name.branchCode  }}</h1>
              
            </div> -->
            
<div>
  <h3 class="font-bold mt-10 text-center mb-5">فهرست شعب </h3>
</div>


<div  class="relative w-full overflow-x-auto shadow-md sm:rounded-lg">
  <div v-if="showNewBranch" class="mt-5">
  <form  @submit.prevent="NewBranch" class=" max-w-md mx-auto ">
  
  <div class="grid md:grid-cols-2 md:gap-6">
    <div class="relative z-0 w-full mb-5 group">
        <input v-model="branchCode"
        type="number" name="floating_first_name" id="floating_first_name" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">کد  شعبه </label>
    </div>
    <div class="relative z-0 w-full mb-5 group">
        <input  v-model="branchName"
        type="text" name="floating_last_name" id="floating_last_name" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_last_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">نام شعبه</label>
    </div>
  </div>
  <div class="grid md:grid-cols-2 md:gap-6">
    <div class="relative z-0 w-full mb-5 group">
        <input v-model="branchDgree"
        type="text"  name="dgree" id="floating_phone" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " required />
        <label for="floating_phone" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">درجه شعبه</label>
    </div>
    <div class="relative z-0 w-full mb-5 group">
        <input  v-model="branchPersonNo"
         type="number" name="floating_company" id="floating_company" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="" required />
        <label for="floating_company" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">تعداد پرسنل</label>
    </div>
  </div>
  <button type="submit" class=" text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> ثبت </button>
</form>
</div>
    <table class=" w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">
            <tr >
                <th scope="col" class="px-6 py-3">
                    نام شعبه
                </th>
                <th scope="col" class="px-6 py-3">
                    کد شعبه
                </th>
                <th scope="col" class="px-6 py-3">
                    درجه شعبه
                </th>
                <th scope="col" class="px-6 py-3">
                    تعداد پرسنل
                </th>
                <th scope="col" class="px-6 py-3">
                    <!-- <span class="sr-only">Edit</span> -->
                </th>
                <th scope="col" class="px-6 py-3">
                  
                  <!-- <a href="/newbranch" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">شعبه جدید</a> -->
                   
                  <button 
            @click="newBranchDefin"      class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
    شعبه جدید 
  </button>

                
                </th>
            </tr>
        </thead>
        
        <tbody>
      


  <tr   v-for=" branch in myBranch " class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-orange-200 dark:hover:bg-gray-600">
      <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ branch.branchName   }}
      </th>
      <td class="px-6 py-4">
          {{ branch.branchCode}}
      </td>
      <td class="px-6 py-4">
        {{ branch.branchDgree}}
      </td>
      <td class="px-6 py-4">
        {{ branch.branchPersonNo}}
      </td>
      <td class="px-6 py-4 text-right">
          <!-- <a  href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">ویرایش</a> -->
          <button  @click.prevent="updateBranchDefin(branch.branchCode , branch.branchName , branch.branchDgree , branch.branchPersonNo)" 
                        class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" >
          ویرایش 
          
        </button>
      </td>
      <td class="px-6 py-4 text-right">
          <!-- <a @click="deleBranch" href="/branch" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">حذف</a> -->
        
          <button  @click.prevent="delBranch(branch.branchCode)" 
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
  import { allBranches } from "../queries";
  import MenuSection from "../components/Menu.vue"

  import { DELETE_BRANCH , NEW_BRANCH , UPDATE_BRANCH } from '@/mutaions'
  import { useUserStore } from "@/user/user";

  
  
 

  export default {

    name : "BarnchView" ,
    
    data() {
      return {
        loginUser: useUserStore(),

        showModal: false ,
        myBranch: null,
        deleleBranch: 0 ,
        showNewBranch : false,

        branchCode : 0 ,
        branchName : "" ,
        branchDgree : "" ,
        branchPersonNo : 0 ,

        isEdit : false , 
        mutateBranch : NEW_BRANCH
        
      };
    },
  
    components :{
      MenuSection,

        
    },
    methods:{

      async NewBranch() {
        
        const newbarnch1 = await this.$apollo.mutate({

          mutation: this.mutateBranch ,
          
                  
                  
            variables: {

              branchCode : this.branchCode ,
              branchName : this.branchName ,
              branchDgree : this.branchDgree ,
              branchPersonNo : this.branchPersonNo ,

            },
        })
        
        location.reload();

      
    },

   


    async  delBranch(brCode){
      if(this.loginUser.token ){
        
        if (window.confirm(" آیا از حذف شعبه مطمئن هستید")){

          const deleteInfo = await this.$apollo.mutate({
          mutation: DELETE_BRANCH,
          variables: {
  
            branchCode : brCode ,
          }
        });
                location.reload();
        }
        }else{
        alert("شما وارد سیستم نشده اید")
        }
      
    },
      
      closeModal(){
        this.showModal = false
      },

    refreshPage()  {
        location.reload(); // Reloads the current page
    },
    newBranchDefin() {

      if(this.loginUser.token ){

          this.showNewBranch = !this.showNewBranch
        }else{
          this.showNewBranch = false
          alert("شما وارد سیستم نشده اید")
      }
      this.branchCode = 0 ,
      this.branchName = "" ,
        this.branchDgree = "" ,
        this.branchPersonNo = 0 ,
      this.mutateBranch = NEW_BRANCH

    },
    updateBranchDefin(branchCode , branchName , branchDgree ,branchPersonNo) {
      if(this.loginUser.token ){

        this.showNewBranch = !this.showNewBranch
      }else{
        this.showNewBranch = false
        alert("شما وارد سیستم نشده اید")
      }
      this.branchCode = branchCode
      this.branchName = branchName
      this.branchDgree = branchDgree
      this.branchPersonNo = branchPersonNo
      this.mutateBranch = UPDATE_BRANCH

    }


    },
  
    async created() {
      const siteInfo = await this.$apollo.query({
        query: allBranches,
      });
      this.myBranch = siteInfo.data.allBranches;
    },

    

    
  };


  </script>