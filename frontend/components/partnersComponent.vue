<template>
  <v-row dense class="justify-center">
    <v-col
      v-for="i in partners"
      :key="i.id"
      loading
      cols="12"
      xs="6"
      sm="4"
      md="3"
      lg="2"
    >
      <v-tooltip bottom>
        <template #activator="{ on, attrs }">
          <a :href="i.url" target="_blank" v-bind="attrs" v-on="on">
            <v-img height="50" contain :src="i.logo" :alt="i.name"></v-img>
          </a>
        </template>
        <span>{{ i.name }}</span>
      </v-tooltip>
    </v-col>
  </v-row>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  name: 'WelcomeComponent',
  auth: false,
  data() {
    return {
      partners: [],
    }
  },
  mounted() {
    this.getPartners()
  },
  methods: {
    async getPartners() {
      const partners = await this.$axios.$get('custom-content/partners/')
      this.partners = partners
    },
  },
})
</script>
