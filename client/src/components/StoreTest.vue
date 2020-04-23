
<!--
    Copyright (C) Sabastian Peters 2020
-->


<template>
    <div>
        My Some Value: {{ someValue }}
    </div>
</template>





<script>

import { createNamespacedHelpers } from 'vuex'
const { mapState, mapActions } = createNamespacedHelpers('telemetry')

export default {
    computed: {
        ...mapState({
            someValue: state => state.someValue
        })
    }
}


</script>





<style>

</style>