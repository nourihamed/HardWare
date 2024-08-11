// import './assets/main.css'
import '../src/style.css'

import { createApp, provide , h , render} from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import 'flowbite' 

import { apolloProvider } from "../src/apollo-config";



const app = createApp(App)
// const app = createApp(App)


app.use(createPinia())
app.use(router)
app.use(apolloProvider)

app.mount('#app')
