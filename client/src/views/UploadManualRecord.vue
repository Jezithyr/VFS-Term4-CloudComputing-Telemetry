<template>
  <div>
    <form>
      Session Id <input v-model="sessionId" type="text" placeholder="Session Id">
      Username <input v-model="userName" type="text" placeholder="Username">
      Position X <input v-model="xPos" type="text" placeholder="Position X">
      Position Y <input v-model="yPos" type="text" placeholder="Position Y">
      Value <input v-model="value" type="text" placeholder="Value">
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
    xPos: 0,
    yPos: 0,
    value: 0
  }),
  methods: {
    upload: function (){
      Datastore.send({
        date: moment().utc().toISOString(),
        sessionId: this.sessionId,
        user: this.userName,
        x: this.xPos,
        y: this.yPos,
        value: this.value
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
