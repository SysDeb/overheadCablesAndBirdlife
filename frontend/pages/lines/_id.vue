<template>
  <div>
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%"> <map-component /> </v-col
      ><v-col> <data-line-detail :data="data" /> </v-col
    ></v-row>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item>
        <data-line-detail :data="data" />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  name: 'LineDetailPage',
  /**
   * asyncData(): Method that gather data before page be created
   *
   * @param {$axios, params} $axios allows to send request to data through $axios, and params
   * allows to access the selected Line id from URL
   * (with page "lines/_id.vue" => "https://path/lines/7" => id = 7)
   */
  async asyncData({ $axios, params }) {
    return {
      data: await $axios.$get(`cables/infrastructures/${params.id}`),
    }
  },
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // small drawer when opening by default
    }
  },
})
</script>
