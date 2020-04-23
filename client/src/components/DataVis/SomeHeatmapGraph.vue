<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <CustomGraph :graphData="graphData" />
</template>




<script>

import CustomGraph from './CustomGraph.vue'
import { mapState } from 'vuex'


export default {
    

    data: () => ({
    }),

    components: {
        CustomGraph
    },

    computed: {

        ...mapState("telemetry", {
            entityList: state => state.entityList
        }),

        graphData: function(){
            let xData = [];
            let yData = [];
            let data = [];
            let startX = Math.min(...this.entityList.map(x => x.x));
            let startY = Math.min(...this.entityList.map(x => x.y));
            let endX = Math.max(...this.entityList.map(x => x.x));
            let endY = Math.max(...this.entityList.map(x => x.y));
            for (var i = startX; i < endX+1; i++) {
                xData.push(i);
            }
            for (var j = startY; j < endY+1; j++) {
                yData.push(j);
            }
            for(let entity of this.entityList){
                data.push([entity.x, entity.y, entity.value]);
            }

            let min = Math.min(...this.entityList.map(x => x.value));
            let max = Math.max(...this.entityList.map(x => x.value));

            return {
                title: {
                    text: "value at position (x,y)",
                    left: 'center'
                },
                grid: {
                    right: 0,
                    left: 80
                },
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
                    min: min,
                    max: max,
                    calculable: true,
                    realtime: false,
                    inRange: {
                        color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                    }
                },
                series: [{
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