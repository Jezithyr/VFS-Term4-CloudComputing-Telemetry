import Vue from 'vue'
import VueRouter from 'vue-router'

// Views
import Landing from '@/views/Landing.vue'
import UploadManualRecord from '@/views/UploadManualRecord.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Landing
  },
  {
    path: '/admin/upload',
    component: UploadManualRecord
  }
]

const router = new VueRouter({
  routes
})

export default router
