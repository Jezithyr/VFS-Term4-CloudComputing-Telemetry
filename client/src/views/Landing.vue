<template>
  <div class="home">
    hey
    <button @click="download">update list</button>
    <div>
      {{ entityList }}
    </div>
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

      // gets the entity list and stores it in vue variable
      let response = await Datastore.get();
      this.entityList = response.data.entityList;
    }
  }
};
</script>
