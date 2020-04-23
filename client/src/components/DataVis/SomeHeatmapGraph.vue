<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <CustomGraph :graphData="graphData" />
</template>




<script>

import CustomGraph from './CustomGraph.vue'


export default {
    

    data: () => ({
    }),

    components: {
        CustomGraph
    },

    methods: {
        generateData() {
        }
    },

    computed: {
        graphData: function(){
            let xData = [];
            let yData = [];
            let data = [];
            let width = 10;
            let height = 10;
            for (var i = 0; i <= width; i++) {
                for (var j = 0; j <= height; j++) {
                    data.push([i, j, Math.sin(i)/width*2 + 0.3 + j/height/2]);
                }
                xData.push(i);
            }
            for (var j = 0; j < height; j++) {
                yData.push(j);
            }

            return {
                tooltip: {},
                xAxis: {
                    type: 'category',
                    data: xData
                },
                yAxis: {
                    type: 'category',
                    data: yData
                },
                visualMap: {
                    min: 0,
                    max: 1,
                    calculable: true,
                    realtime: false,
                    inRange: {
                        color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                    }
                },
                series: [{
                    name: 'Gaussian',
                    type: 'heatmap',
                    data: data,
                    emphasis: {
                        itemStyle: {
                            borderColor: '#333',
                            borderWidth: 1
                        }
                    },
                    progressive: 1000,
                    animation: false
                }]
            }
        }
    }
}

</script>