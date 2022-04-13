<template>
  <v-container fluid fill-height>
    <v-col cols="12" lg="9">
      <v-layout align-center justify-center>
        <v-flex
          ><v-col cols="12"
            ><v-row justify="center" align="center">
              <v-col cols="12" class="justify-center mb-10" align="center">
                <div class="text-h2 mb--1">
                  {{ $t('app.app-name') }}
                </div>
              </v-col>
              <v-col cols="12">
                <partners-component />
              </v-col> </v-row
          ></v-col>
        </v-flex>
      </v-layout>
    </v-col>
    <v-col cols="12" lg="3"><posts-list /></v-col>
  </v-container>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
})
</script>
