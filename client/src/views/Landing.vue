<template>
  <div>
    <button @click="download">refresh list</button>
    <table>
      <thead>
        <th>Date</th>
        <th>Session Id</th>
        <th>Username</th>
      </thead>
      <tbody>
        <tr v-for="(entity, index) in entityList" :key="index">
          <td>{{ entity.date }}</td>
          <td>{{ entity.sessionId }}</td>
          <td>{{ entity.user }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>



<script>
import Datastore from "@/lib/Datastore.js";
import moment from "moment";

export default {
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
  }
};
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