
/*
    Copyright (C) Sabastian Peters 2020
*/


import Vue from 'vue'
import Vuex from 'vuex'


// Import Vuex Modules

import echarts from "./modules/echarts.js"
import telemetry from './modules/telemetry.js';


const debug = process.env.NODE_ENV !== 'production'



Vue.use(Vuex)


export default new Vuex.Store({
    modules: {
        telemetry,
        echarts
    },
    strict: debug
})
