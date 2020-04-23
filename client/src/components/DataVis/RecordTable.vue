

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
                <th v-for="(format, key, j) in entityFormat" :key="j">
                    {{ format.displayName }}
                </th>
            </thead>
            <tbody>
                <tr v-for="(entity, index) in entityList" :key="index">
                    <td v-for="(format, key, j) in entityFormat" :key="j">
                        {{ entity[key] }}
                    </td>
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
            "isFetchingData",
            "entityFormat"
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