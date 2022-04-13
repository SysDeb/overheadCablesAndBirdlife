
<template>
  <div>
    <v-radio-group v-model="display" row dense @change="source">
      <v-row justify="space-around">
        <v-radio :label="$t('display.all')" value="both"></v-radio>
        <v-radio :label="$t('support.supports-eqmt')" value="poles"></v-radio>
        <v-radio
          :label="$t('display.lines-eqmt')"
          value="segments"
        ></v-radio></v-row
    ></v-radio-group>
    <v-data-table
      :headers="headers"
      :items="selectedData"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>


<script lang='ts'>
import { mapGetters } from 'vuex'
import Vue from 'vue'

export default Vue.extend({
  name: 'EquipmentDisplay',

  data() {
    return {
      display: 'both',
      selectedData: [],
      headers: [
        {
          text: this.$t('app.id'),
          align: 'start',
          sortable: true,
          value: 'id',
        },
      ],
    }
  },
  async fetch() {
    const pointOpData = await this.$axios.$get(
      'cables/operations/?type_model=point'
    )
    const lineOpData = await this.$axios.$get(
      'cables/operations/?type_model=line'
    )
    const opData = await this.$axios.$get('cables/operations')
    this.$store.commit('cablesStore/addOperation', {
      all: opData,
      point: pointOpData,
      line: lineOpData,
    })
    // needed to load data at start
    this.selectedData = this.opData
  },
  computed: mapGetters({
    opData: 'cablesStore/opData',
    pointOpData: 'cablesStore/pointOpData',
    lineOpData: 'cablesStore/lineOpData',
  }),
  methods: {
    source(choice: string) {
      switch (choice) {
        case 'both':
          this.selectedData = this.opData
          break
        case 'poles':
          this.selectedData = this.pointOpData
          break
        case 'segments':
          this.selectedData = this.lineOpData
          break
        default:
        // TODO raise an exception and handle it or display message to user
      }
    },
  },
})
</script>
