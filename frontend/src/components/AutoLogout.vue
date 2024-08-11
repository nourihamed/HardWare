<template>
    <div>

    </div>
</template>


<script>
import { useUserStore } from "@/user/user";
export default {
    setup() {
        
    },
    name : "AutoLogout",

    data(){
        return{
            events : ['click' , 'mousemove' , 'mousedown' , 'scroll' , 'keypress' , 'load'] ,
            warningTimer : null ,
            logoutTimer : null ,
            loginUser: useUserStore()
        }
    },

    beforeUpdate(){
        this.events.forEach( (e) => window.addEventListener(e , this.resetTimer) );
        

        this.resetTimer()
    },

    mounted(){
        
        this.events.forEach( (e) => window.addEventListener(e , this.resetTimer) );
        

        this.setTimer()
    },
    methods:{

        setTimer(){
            this.warningTimer = setTimeout(this.warningMessage , 10*60*1000)
            this.logoutTimer = setTimeout(this.userSignOut , 10*60*1000)
        },
        
        warningMessage(){
            alert('دوباره وارد سیستم شوید')
        },
        resetTimer() {
            clearTimeout(this.warningTimer);
            clearTimeout(this.logoutTimer);
            this.setTimer()

        },
        async userSignOut() {
            clearTimeout(this.warningTimer);
            this.loginUser.removeToken()
        },
    }
}
</script>