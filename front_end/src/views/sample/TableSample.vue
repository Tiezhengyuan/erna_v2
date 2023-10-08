<template>
  <div class="container table-sample">
    <table border="1">
      <caption v-show="loaded_samples.length > 0">
        Samples of the study {{ study_name }}
      </caption>
      <thead>
        <tr>
          <th v-for="(name, h) in sample_header" :key="h">{{ name }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(values, s) in loaded_samples" :key="s">
          <td v-for="(val, i) in values" :key="i">{{ val }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "TableSample",
  computed: {
    ...mapState(["study_name", "loaded_samples"]),
    sample_header() {
      if (this.loaded_samples.length > 0){
        return Object.keys(this.loaded_samples[0]);
      }
      return []
    },
  },
};
</script>

<style scoped>
.container.table-sample {
  background-color: white;
}
</style>
