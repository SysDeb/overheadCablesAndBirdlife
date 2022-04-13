<template>
  <v-container fluid fill-height style="background-color: yellow">
    <v-row
      class="text-center fill-height"
      fill-height
      style="background-color: blue"
    >
      <v-col cols="12" fill-height style="background-color: red">
        <v-card
          class="d-flex pa-2 d-flex align-stretch fill-height"
          outlined
          fill-height
          tile
          style="background-color: green"
        >
          <div>flexbox</div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  name: 'HelloWorld',

  data: () => ({}),
})
</script>
