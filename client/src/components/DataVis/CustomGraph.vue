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

    props: {
        graphData: Object
    },

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