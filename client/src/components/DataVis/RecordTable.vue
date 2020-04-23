

<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <div class="parent">
        <div v-if="isFetchingData == true">
            loading...
        </div>
        <div v-else-if="entityList.length <= 0">
            No data to show
        </div>
        <table v-else>
            <thead>
                <th v-for="(format, key, j) in entityFormat" :key="j">
                    {{ format.displayName }}
                </th>
            </thead>
            <tbody>
                <tr v-for="(entity, index) in filteredEntityList" :key="index">
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
        ]),
        filteredEntityList: function (){

            // makes a copy of the list and sorts it
            return [...this.entityList].sort((a, b) => {
                if(a.date < b.date) return 1;
                if(b.date < a.date) return -1;
                return 0
            })
        }
    },
}

</script>


<style scoped>

.parent {
  margin: 16px;
}

table {
  width: 100%;
}

td {
  padding: 12px;
}

</style>