<template>
  <div class="home">
    hey
    <button @click="download">update list</button>
  </div>
</template>



<script>
import Datastore from "@/lib/Datastore.js";
import moment from "moment";

export default {
  methods: {
    download: async () => {
      let list = await Datastore.get();
      console.log(list);
    }
  }
};
</script>
