<template>
  <v-snackbar v-model="display">
    ERR-{{ err.code }}: {{ err.msg }}

    <template #action="{ attrs }">
      <v-btn color="pink" text v-bind="attrs" @click="display = !display">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script lang='ts'>
import Vue from 'vue'
import { mapGetters } from 'vuex'

export default Vue.extend({
  data() {
    return {
      display: false,
    }
  },
  computed: {
    /**
     * Getter for "err" (error Object) from errorStore
     */
    ...mapGetters({
      err: 'errorStore/err',
    }),
  },
  watch: {
    /**
     * Watcher: when value changes, that triggers display of the error message in snackbar.
     */
    err() {
      this.display = true
    },
  },
})
</script>
