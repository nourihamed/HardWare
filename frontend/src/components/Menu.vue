<template>
<div>
    <form  >
    <nav class="bg-white border-gray-200 dark:bg-gray-900">
        <div class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4">
            <a href="http://bank-maskan.ir" class="flex items-center space-x-3 rtl:space-x-reverse">
                <img src="../assets/bank-maskan.svg" class="h-8" alt="لگو" />
                <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">بانک مسکن</span>
            </a>
            <div class="flex items-center space-x-6 rtl:space-x-reverse">
                <a href="tel:04135299000" class="text-sm  text-gray-500 dark:text-white hover:underline">(041) 35299000</a>
                <!-- <a href="" class="text-sm  text-blue-600 dark:text-blue-500 hover:underline">ورود</a> -->
                <button 
                 data-modal-target="authentication-modal" data-modal-toggle="authentication-modal" class=" block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
        <h1 v-if="loginUser.token" > 

            {{ loginUser.getUser.lastName    }}  {{ loginUser.getUser.username    }}  
        </h1>
        <h1 v-else> ورود</h1>
  </button>
  <button 
            @click="userSignOut"      class="block text-blue-700 hover:text-orange-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
    خروج 
  </button>
            </div>
        </div>
    </nav>
    <nav class="bg-gray-50 dark:bg-gray-700">
        <div class="max-w-screen-xl px-4 py-3 mx-auto">
            <div class="flex items-center">
                <ul class="flex flex-row font-medium mt-0 space-x-8 rtl:space-x-reverse text-sm">
                    <li>
                        <a href="home" class="text-gray-900 dark:text-white hover:underline" aria-current="page">صفحه اصلی</a>
                    </li>
                    <li>
                        <a href="branch" class="text-gray-900 dark:text-white hover:underline">شعب</a>
                    </li>
                    <li>
                        <a href="company" class="text-gray-900 dark:text-white hover:underline">شرکت‌های پشتیبان</a>
                    </li>
                    <li>
                        <a href="category" class="text-gray-900 dark:text-white hover:underline">دسته بندی</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main modal -->
  <div id="authentication-modal" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
      <div class="relative p-4 w-full max-w-md max-h-full">
          <!-- Modal content -->
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
              <!-- Modal header -->
              <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                  <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            ورود به سامانه    
                  </h3>
                  <button type="button" class="end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="authentication-modal">
                      <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                      </svg>
                      <span class="sr-only">Close modal</span>
                  </button>
              </div>
              <!-- Modal body -->
              <div class="p-4 md:p-5">
                  <form  @submit.prevent="userSignIn" class="space-y-4" action="#" >
                      <div>
                          <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">نام کاربری</label>
                          <input 
                          v-model="signInDetails.username"
                          type="text" name="username" id="username" 
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="شماره پرسنلی" required />
                      </div>
                      <div>
                          <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">کلمه عبور</label>
                          <input v-model="signInDetails.password"  
                          type="password" name="password" id="password" placeholder="••••••••" 
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required />
                      </div>
                      <div class="flex justify-between">
                          <!-- <div class="flex items-start">
                              <div class="flex items-center h-5">
                                  <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800" required />
                              </div>
                              <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Remember me</label>
                          </div> -->
                          <!-- <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">فراموشی رمز؟</a> -->
                      </div>
                      <button type="submit" data-modal-hide="authentication-modal" class=" w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" :class="isHidden">ورود</button>
                      <!-- <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                          Not registered? <a href="#" class="text-blue-700 hover:underline dark:text-blue-500">Create account</a>
                      </div> -->
                  </form>
              </div>
          </div>
      </div>
  </div> 
</form>
</div>    


</template>

<script>
import { useUserStore } from "@/user/user";
import { USER_SIGNIN } from "@/mutaions";








export default {

    name : "MenuSection",
    
    setup() {
        
   
  },




    
  data() {
    return {
       isHidden : true , 
      signInDetails: {
        isAuthenticated: false,
        username: "",
        password: "",
      },

      loginText : "ورود",
      loginUser: useUserStore()
    };
  },
  methods: {
    async userSignIn() {
        const user = await this.$apollo.mutate({
            mutation: USER_SIGNIN,
            variables: {
                username: this.signInDetails.username,
                password: this.signInDetails.password,
            },
        });
        
        // console.log(this.signInDetails)
        this.loginUser.setToken(user.data.tokenAuth.token);
        this.loginUser.setUser(user.data.tokenAuth.user);

      
    },
    
    async userSignOut() {

        
        // console.log(this.signInDetails)
        this.loginUser.removeToken()

        

  

      
    },
    
  },
};

</script>