

<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <div class="parent">
        <div v-if="isFetchingData == true">
            loading...
        </div>
        <table v-else>
            <thead>
                <th>Date</th>
                <th>Session Id</th>
                <th>Username</th>
                <th>Position X</th>
                <th>Position Y</th>
                <th>Value</th>
            </thead>
            <tbody>
                <tr v-for="(entity, index) in entityList" :key="index">
                    <td>{{ entity.date }}</td>
                    <td>{{ entity.sessionId }}</td>
                    <td>{{ entity.user }}</td>
                    <td>{{ entity.x }}</td>
                    <td>{{ entity.y }}</td>
                    <td>{{ entity.value }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>



<script>

import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions } = createNamespacedHelpers('telemetry')

export default {
    props: {
        entityList: Array
    },
    computed: {
        ...mapState([
            "isFetchingData"
        ])
    },
}

</script>


<style scoped>

.parent {

  margin: 16px;

  /* Centers table */
  margin-left:auto; 
  margin-right:auto;
}

td {
  padding: 12px;
}

</style>