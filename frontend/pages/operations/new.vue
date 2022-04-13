<template>
  <div style="height: 90vh" class="overflow-auto">
    <v-row v-if="$vuetify.breakpoint.lgAndUp"
      ><v-col width="50%">
        <map-component :edit-mode="true" mode="point" /> </v-col
      ><v-col><form-point-component /></v-col
    ></v-row>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> {{ $t('app.map') }} </v-tab>
      <v-tab-item>
        <map-component :edit-mode="true" mode="point" />
      </v-tab-item>
      <v-tab> {{ $t('app.data') }} </v-tab>
      <v-tab-item> <form-point-component /> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  name: 'PointPage',
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
})
</script>
