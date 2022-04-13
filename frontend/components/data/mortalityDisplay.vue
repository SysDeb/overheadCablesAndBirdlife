
  <template>
  <div></div>
  <!-- <v-data-table
    :headers="headers"
    :items="mortalityData"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table> -->
</template>

<script lang='ts'>
import Vue from 'vue'
// import { FeatureCollection } from 'geojson'
export default Vue.extend({
  name: 'MortalityDisplay',
  // props: { mortalityData: FeatureCollection },

  data() {
    return {
      headers: [
        {
          text: 'ID Mortalité',
          align: 'start',
          sortable: true,
          value: 'properties.id',
        },
        // { text: 'Entité', value: 'properties.owner.label' },
      ],
    }
  },
})
</script>
