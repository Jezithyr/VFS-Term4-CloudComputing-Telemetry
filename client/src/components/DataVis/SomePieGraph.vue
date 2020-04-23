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
            series: [{
                data: [
                    { value: 820, name: "a" },
                    { value: 932, name: "b" },
                    { value: 901, name: "c" },
                    { value: 934, name: "d" },
                    { value: 1290, name: "e" },
                    { value: 1330, name: "f" },
                    { value: 1320, name: "g" }
                ],
                type: 'pie'
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




<style scoped>
.echarts {
    width: 100%;
    height: 100%;
}
</style>