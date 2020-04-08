<template>
  <div>
    <h1>Create a manual record to upload</h1>
    <button @click="upload">Upload</button>
  </div>
</template>

<script>
import Datastore from "@/lib/Datastore.js";
import moment from "moment";

export default {
  methods: {
    upload: () => {
      Datastore.send({
        "date": moment().utc().toISOString(),
        "user": "Sabastian",
        "asdasd": "Hey"
      });
    }
  }
};
</script>
