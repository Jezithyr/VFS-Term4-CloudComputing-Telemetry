<template>
    <div>
        
        <StoreTest/>
        
        <button @click="download">refresh list</button>
        <RecordTable :entityList="this.entityList" />
    </div>
</template>



<script>

// Components
import StoreTest from "@/components/StoreTest.vue"
import RecordTable from "@/components/DataVis/RecordTable.vue"

// Libs
import Datastore from "@/lib/Datastore.js";


export default {

    components: {
        StoreTest,
        RecordTable
    },
    
    data: () => ({
        entityList: []
    }),

    methods: {
        download: async function (){ // NOTE: the function keyword needs to be here to access the entity lsit

            this.entityList = [{
                date: "loading...",
            }]

            // gets the entity list and stores it in vue variable
            let response = await Datastore.get();
            this.entityList = response.data.entityList;
        }
    },

    beforeMount: function(){
        this.download();
    },
    
};
</script>