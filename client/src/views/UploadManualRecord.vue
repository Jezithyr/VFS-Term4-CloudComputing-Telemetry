<template>
    <div>
        <form>
            <div class="input-container" v-for="(format, key, j) in fieldList" :key="j">
                <div class="input-label"> {{ format.displayName }} </div>
                <input :v-model="key" type="text" :placeholder="format.displayName" />
            </div>

            <button @click="upload">Upload</button>
        </form>
    </div>
</template>

<script>



import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions } = createNamespacedHelpers('telemetry')



import Datastore from "@/lib/Datastore.js";
import moment from "moment";

export default {
    
    data: () => ({
        sessionId: "",
        userName: "",
        x: 0,
        y: 0,
        value: 0
    }),

    // TODO: move this code to Vuex, it will work without it, but it's important to be consistant (plus will save me time later)
    methods: {
        upload: function() {
            Datastore.send({
                date: moment().utc().toISOString(),
                sessionId: this.sessionId,
                user: this.userName,
                x: this.x,
                y: this.y,
                value: this.value
            });
        }
    },

    computed: {
        ...mapState([
            "entityFormat"
        ]),
        fieldList: function() {
            let fieldList = {...this.entityFormat}; /// make a copy of the object
            delete fieldList.date; /// we don't want user to add the date (only removes the reference)
            return fieldList;
        }
    },

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

.input-container {
    display: flex;
    flex-flow: row;
}

.input-label {
    width: 100px;
    overflow: hidden;
    text-align: left;
}

</style>
