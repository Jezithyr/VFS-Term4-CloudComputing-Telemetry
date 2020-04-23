<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <CustomGraph :graphData="graphData"/>
</template>




<script>

import CustomGraph from './CustomGraph.vue'


export default {
    
    components: {
        CustomGraph
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
}

</script>