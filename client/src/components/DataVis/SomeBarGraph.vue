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
    
    components: {
        CustomGraph
    },

    computed: {
        ...mapState("telemetry", {
            entityList: state => state.entityList
        }),

        graphData: function (){

            
            // calculates the total points per player
            let userListData = {};
            for(let entity of this.entityList){
                if(userListData[entity.user] == undefined) userListData[entity.user] = 0;
                userListData[entity.user] = Number(userListData[entity.user]) + Number(entity.value);
            }

            // moves that data into a form echarts can read
            let data = [];
            let axisLabels = [];
            for(let user in userListData){
                data.push(userListData[user])
                axisLabels.push(user);
            }

            // creates the chart obj
            return {
                title: {
                    text: "value per user",
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
                    type: 'bar'
                }]
            }
        }
    }

    
}

</script>