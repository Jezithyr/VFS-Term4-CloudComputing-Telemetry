<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <v-chart 
        :theme="theme"
        :autoresize="true"
        :options="graphData"/>
</template>




<script>

import { mapState } from 'vuex'
import ECharts from 'vue-echarts'

export default {
    
    name: "LineGraphExample",

    components: {
        'v-chart': ECharts
    },

    data: () => ({
        graphData: {
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                data: [820, 932, 901, 934, 1290, 1330, 1320],
                type: 'line'
            }]
        }
    }),

    computed: {
        ...mapState("echarts", {
            theme: state => state.theme
        })
    },
}

</script>




<style>

</style>