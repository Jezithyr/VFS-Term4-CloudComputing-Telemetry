<template>
    <div>
        
        <StoreTest/>
        
        <button @click="fetchEntityList">refresh list</button>
        <RecordTable :entityList="this.entityList" />
    </div>
</template>



<script>

// Components
import StoreTest from "@/components/StoreTest.vue"
import RecordTable from "@/components/DataVis/RecordTable.vue"

// Libs
import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions } = createNamespacedHelpers('telemetry')


export default {

    components: {
        StoreTest,
        RecordTable
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