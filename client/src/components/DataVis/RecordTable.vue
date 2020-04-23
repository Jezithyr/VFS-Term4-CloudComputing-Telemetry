

<!--
    Copyright (C) Sabastian Peters 2020
-->

<template>
    <div>

        <table>
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

export default {
    props: {
        entityList: Array
    }
}

</script>


<style scoped>

table {

  margin: 16px;

  /* Centers table */
  margin-left:auto; 
  margin-right:auto;
}

td {
  padding: 12px;
}

</style>