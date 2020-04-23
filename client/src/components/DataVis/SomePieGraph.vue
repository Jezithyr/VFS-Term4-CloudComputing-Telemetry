<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <CustomGraph :graphData="graphData"/>
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
                userListData[entity.user] = Number(userListData[entity.user]) + 1;
            }

            // moves that data into a form echarts can read
            let data = [];
            let axisLabels = [];
            for(let user in userListData){
                data.push({
                    value: userListData[user],
                    name: user,
                })
                axisLabels.push(user);
            }

            // creates the chart obj
            return {
                title: {
                    text: "records per user",
                    left: 'center'
                },
                series: [{
                    type: 'pie',
                    data: data,
                    radius: '55%',
                    center: ['50%', '50%'],
                    label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                    },
                }]
            }
        }
    }
}

</script>