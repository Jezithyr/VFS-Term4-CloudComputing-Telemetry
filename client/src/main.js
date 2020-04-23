
/*
  Copyright (C) Sabastian Peters 2020
*/



// ## SETUP VUE ##

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false





// ## SETUP E-CHARTS ##

import ECharts from 'vue-echarts' // refers to components/ECharts.vue in webpack

// import ECharts modules manually to reduce bundle size (don't do this in component)
import 'echarts/lib/chart/line'
import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/pie'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/toolbox'

Vue.component('v-chart', ECharts)





// ## START VUE ##

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
