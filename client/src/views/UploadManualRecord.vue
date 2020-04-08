<template>
  <div>
    <form>
      <input v-model="sessionId" type="text" placeholder="Session Id">
      <input v-model="userName" type="text" placeholder="Username">
      <button @click="upload">Upload</button>
    </form>
  </div>
</template>

<script>
import Datastore from "@/lib/Datastore.js";
import moment from "moment";

export default {
  data: () => ({
    sessionId: "",
    userName: "",
  }),
  methods: {
    upload: function (){
      Datastore.send({
        date: moment().utc().toISOString(),
        sessionId: this.sessionId,
        user: this.userName
      });
    }
  }
};
</script>

<style scoped>

form {
  display: flex;
  flex-flow: column;
  align-items: center;

  padding: 4px;
}

form > * {
  margin: 8px;
}


</style>
