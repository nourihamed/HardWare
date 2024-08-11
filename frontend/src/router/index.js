import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BarnchView from '../views/BranchView.vue'

import SupportCompany from '../views/SupportCompany.vue'
import CategoryView from '../views/CategoryView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView ,
      
    },
    {
      path: '/branch',
      name: 'branch',
      component: BarnchView,
      
    },
    
    {
      path: '/company',
      name: 'company',
      component: SupportCompany
    },
    {
      path: '/category',
      name: 'category',
      component: CategoryView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
