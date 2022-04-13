<template>
  <v-container fill-height fluid class="pa-0">
    <v-row v-if="$vuetify.breakpoint.mdAndUp" class="fill-height">
      <v-col cols="6" class="pr-0 pt-0 pb-0">
        <map-component :edit-mode="false" />
      </v-col>
      <v-col cols="6" class="pa-0">
        <display-component />
      </v-col>
    </v-row>
    <!-- <template v-slot:extension>
        <v-tabs
          fixed-tabs
          class="fill-height"
          background-color="indigo"
          dark
          v-model="tab"
        >
          <v-tab> {{ $t('app.map') }} </v-tab>
          <v-tab> {{ $t('app.data') }} </v-tab>
        </v-tabs>
      </template>
      <v-tab-items v-model="tab">
        <v-tab-item>
          <map-component :edit-mode="false" />
        </v-tab-item>
        <v-tab-item>
          <display-component />
        </v-tab-item>
      </v-tab-items> -->
    <template v-if="!$vuetify.breakpoint.mdAndUp">
      <v-tabs v-model="tab" align-with-title fixed-tabs>
        <v-tab> {{ $t('app.map') }} </v-tab>
        <v-tab> {{ $t('app.data') }} </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="fill-height">
        <v-tab-item>
          <map-component :edit-mode="false" />
        </v-tab-item>
        <v-tab-item>
          <display-component />
        </v-tab-item>
      </v-tabs-items>
    </template>
  </v-container>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  name: 'ViewComponent',
  data() {
    return {
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
      tab: null,
      items: ['web', 'shopping', 'videos', 'images', 'news'],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },
  mounted() {
    /**
     * Call of "loadNomenclatures" action from nomenclaturesStore to load Nomenclatures needed to
     * get data to set up the application.
     * Implemented here as authentification needed
     */
    this.$store.dispatch('nomenclaturesStore/loadNomenclatures')
    /**
     * Call of "addPointCoord" action from coordinatesStore to linitialize newPointCoord at null
     */
    this.$store.commit('coordinatesStore/addPointCoord', {
      lat: null,
      lng: null,
    })
  },
  /**
   * openDrawer(): Method to manage opening/closing drawer menu
   */
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
  },
})
</script>
