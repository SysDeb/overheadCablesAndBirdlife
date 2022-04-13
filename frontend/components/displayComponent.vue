<template>
  <div class="d-flex align-stretch">
    <v-tabs center-active grow color="indigo">
      <v-tab> {{ $t('display.infrastructures') }} </v-tab>
      <v-tab-item>
        <data-infrastructure-display />
      </v-tab-item>
      <v-tab> {{ $t('support.supports-eqmt') }} </v-tab>
      <v-tab-item>
        <data-equipment-display />
      </v-tab-item>
      <v-tab>
        {{ $t('display.sensitive-areas') }}
      </v-tab>
      <v-tab-item>
        <data-sens-area-display />
      </v-tab-item>
      <v-tab> {{ $t('display.mortality-cases') }} </v-tab>
      <v-tab-item>
        <data-mortality-display />
      </v-tab-item>
    </v-tabs>
  </div>
</template>
<script lang='ts'>
export default {
  name: 'DisplayComponent',
}
</script>

<style>
.v-tab {
  width: 100px;
  background-color: 'indigo';
}
</style>
