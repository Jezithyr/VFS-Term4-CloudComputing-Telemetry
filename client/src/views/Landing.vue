<template>
    <div>
        
        <StoreTest/>
        
        <div id="graph-container">
            <SomeLineGraph />
            <SomeBarGraph />
            <SomePieGraph />
            <SomeHeatmapGraph />
        </div>

        <button @click="fetchEntityList">refresh list</button>
        <RecordTable :entityList="this.entityList" />
    </div>
</template>



<script>

// Components
import StoreTest from "@/components/StoreTest.vue"
import RecordTable from "@/components/DataVis/RecordTable.vue"
import SomeLineGraph from "@/components/DataVis/SomeLineGraph.vue"
import SomeBarGraph from "@/components/DataVis/SomeBarGraph.vue"
import SomePieGraph from "@/components/DataVis/SomePieGraph.vue"
import SomeHeatmapGraph from "@/components/DataVis/SomeHeatmapGraph.vue"

// Libs
import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions } = createNamespacedHelpers('telemetry')


export default {

    components: {
        StoreTest,
        RecordTable,
        SomeLineGraph,
        SomeBarGraph,
        SomePieGraph,
        SomeHeatmapGraph
    },
     
    methods: {
        ...mapActions([
            "fetchEntityList"
        ]),
    },
    computed: {
        ...mapState([
            "entityList"
        ])
    },

    beforeMount: function(){
        this.fetchEntityList();
    },
    
};
</script>



<style scoped>

#graph-container {
    display: flex;
    flex-flow: row wrap;
    max-width: 100%;
}

#graph-container > * {
    width: 400px;
    height: 400px;
}

</style>