<template>
  <div>
    <h1>Create a manual record to upload</h1>
    <button @click="upload">Upload</button>
  </div>
</template>

<script>
import Datastore from "@/lib/Datastore.js";

export default {
  methods: {
    upload: () => {
      Datastore.send({
        "date": "2001-13-10",
        "user": "Sabastian",
        "asdasd": "Hey"
      });
    }
  }
};
</script>
