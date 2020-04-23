<template>
  <div>
    <StoreTest/>
    <RecordTable/>
  </div>
</template>



<script>
import StoreTest from "@/components/StoreTest.vue"
import RecordTable from "@/components/DataVis/RecordTable.vue"

export default {

  components: {
    StoreTest,
    RecordTable
  },
  
};
</script>