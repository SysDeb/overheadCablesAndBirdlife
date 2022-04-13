<template>
  <v-card class="fill-height overflow-auto">
    <v-app-bar flat dark color="blue-grey lighten-1">
      <v-app-bar-nav-icon>
        <v-btn icon @click="$router.back()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-app-bar-nav-icon>
      <v-toolbar-title class="text-h6 pl-2">
        {{ $t('support.support') }}
        <strong>{{ data.properties.owner.label }}</strong>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-chip
        class="mr-2"
        dark
        :class="[lastDiag.neutralized ? 'green' : 'red']"
        >{{ lastDiag.neutralized ? 'Neutralisé' : 'A neutraliser' }}</v-chip
      >
    </v-app-bar>

    <v-card-text class="overflow-y-auto fill-height">
      <v-card class="my-2">
        <v-card-title
          >Info Support <v-spacer></v-spacer>
          <v-btn icon @click="$router.push('/view')">
            <v-icon color="orange">mdi-pencil</v-icon>
          </v-btn></v-card-title
        >
        <v-card-text>
          <p class="text-strong" v-if="data.properties.geo_area.length > 0">
            Limites administratives
          </p>

          <v-chip v-for="(ga, index) in data.properties.geo_area" :key="index">
            {{ ga.name }} ({{ ga.code }})
          </v-chip>
          <p v-if="data.properties.sensitive_area.length > 0">
            Zones sensibles
          </p>

          <v-chip v-for="sa in data.properties.sensitive_area" :key="sa.id">
            {{ sa.name }} {{ sa.name }}
          </v-chip>
        </v-card-text>
      </v-card>
      <data-diagnosis-card :diagnosis="lastDiag" />
      <data-operation-card v-if="lastOp" :operation="lastOp" />
      <v-card
        ><v-card-title v-if="previousActions.length" class="font-weight-bold">
          {{ $t('support.history') }}
        </v-card-title>
        <v-expansion-panels>
          <v-expansion-panel v-for="action in previousActions" :key="action.id">
            <v-expansion-panel-header>
              {{ action.resourcetype }} - {{ action.date }}
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <data-diagnosis-card
                v-if="action.resourcetype === 'Diagnosis'"
                :diagnosis="action"
              /><data-operation-card
                v-if="action.resourcetype === 'Operation'"
                :operation="action"
              />
            </v-expansion-panel-content>
          </v-expansion-panel> </v-expansion-panels
      ></v-card> </v-card-text
  ></v-card>
</template>


<script lang="ts">
import { Feature } from 'geojson'
import Vue, { PropOptions } from 'vue'

export default Vue.extend({
  name: 'SupportDetailComponent',
  props: { data: { type: Object, default: null } as PropOptions<Feature> },

  data() {
    let lastDiag: Feature | null = null
    let lastOp: Feature | null = null
    let previousActions: Array<Feature> | null = []
    let update: boolean = false

    return {
      lastDiag,
      lastOp,
      previousActions,
      update,
    }
  },
  created() {
    // Gather last Diagnosis (field last=True)
    this.lastDiag = this.data.properties?.actions_infrastructure.find(
      (action: { resourcetype: string; last: boolean }) =>
        action.resourcetype === 'Diagnosis' && action.last
    )
    // Gather last Operation (field last=True)
    this.lastOp = this.data.properties?.actions_infrastructure.find(
      (action: { resourcetype: string; last: boolean }) =>
        action.resourcetype === 'Operation' && action.last
    )
    // Gather all older actions (Diagnosis and Operations) with field last=False
    this.previousActions = this.data.properties?.actions_infrastructure.filter(
      (action: { last: boolean }) => !action.last
    )
  },
})
</script>
