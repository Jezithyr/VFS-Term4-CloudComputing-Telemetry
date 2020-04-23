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

import ECharts from 'vue-echarts'


export default {
    
    name: "LineGraphExample",
    props: ["theme"],
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
                type: 'bar'
            }]
        }
    })
}

</script>




<style>

</style>