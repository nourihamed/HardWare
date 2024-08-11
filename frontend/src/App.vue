

<template>
<div>
<div>
</div>
<!-- <RouterLink to="/about">About</RouterLink> -->
 <menu-section />
  <RouterView />
  <auto-logout />
</div>
</template>



<script>
import { useUserStore } from "@/user/user";
import MenuSection from "../src/components/Menu.vue"
import AutoLogout from "./components/AutoLogout.vue"



export default {
  

  components :{
    MenuSection,

    AutoLogout
  },

  


  
  }
  

  




</script>
