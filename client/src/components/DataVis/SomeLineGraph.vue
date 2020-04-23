<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <CustomGraph :graphData="graphData"/>
</template>




<script>

import CustomGraph from './CustomGraph.vue'
import { mapState } from 'vuex'
import moment from 'moment'


export default {
    
    components: {
        CustomGraph
    },


    computed: {
        ...mapState("telemetry", {
            entityList: state => state.entityList
        }),

        graphData: function (){

            
            // calculates the total points per player
            let orderedEntityList = [...this.entityList].sort((a, b) => {
                if(a.date < b.date) return -1;
                if(b.date < a.date) return 1;
                return 0
            });

            // moves that data into a form echarts can read
            let data = [];
            let axisLabels = [];
            for(let entity of orderedEntityList){
                data.push(entity.value)
                axisLabels.push(moment(entity.date).format("MM/DD/YY"));
            }

            // creates the chart obj
            return {
                title: {
                    text: "value over time",
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: axisLabels
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: data,
                    type: 'line'
                }]
            }
        }
    }
}

</script>