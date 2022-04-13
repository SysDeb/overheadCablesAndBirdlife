<template>
  <v-data-table
    :headers="headers"
    :items="SADataFeatures"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script lang='ts'>
import { mapGetters } from 'vuex'
import Vue from 'vue'

export default Vue.extend({
  name: 'SensAreaDisplay',
  data() {
    return {
      headers: [
        {
          text: 'ID Zone Sensible',
          align: 'start',
          sortable: true,
          value: 'id',
        },
        { text: 'Name', value: 'properties.name' },
        { text: 'Code', value: 'properties.code' },
      ],
    }
  },
  /** Fetch Sensitive Area from backend and record it to Nuxt Store */
  async fetch() {
    const data = await this.$axios.$get('sensitive-areas/') // get FeatureCollection
    this.$store.commit('saStore/add', data)
  },
  /** Gather Sensitive Area data from Nuxt Store */
  computed: mapGetters({ SADataFeatures: 'saStore/SADataFeatures' }),
})
</script>
