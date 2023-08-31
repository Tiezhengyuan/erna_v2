<template>
  <div class="container table">
    <thead>
      <tr>
        <th>Sample name</th>
        <th>File path (R1)</th>
        <th>File path (R2)</th>
        <th>Delete parsed files</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(sample, i) in samples" :key="i">
        <td>
          <button>Edit</button>
          {{ sample.sample_name }}
        </td>
        <td>{{ sample.R1_file.split(/[\\, //]/).pop() }}</td>
        <td>{{ sample.R2_file.split(/[\\, //]/).pop() }}</td>
        <td>
          <button @click="deleteSample(sample)">Delete</button>
        </td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2">Number of R1 files: {{ R1_num }}</td>
      </tr>
      <tr>
        <td colspan="2">Number of R2 files: {{ R2_num }}</td>
      </tr>
      <tr>
        <td colspan="2">Number of Samples: {{ sample_num }}</td>
      </tr>
    </tfoot>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "TableTwoEnds",
  computed: {
    ...mapState(["samples"]),
    sample_num() {
      const names = this.samples.map((el) => el.sample_name);
      const unique = names.filter((val, index, array) => {
        return array.indexOf(val) == index;
      });
      return unique.length;
    },
    R1_num() {
      const R1_files = this.samples.map((el) => el.R1_file);
      return R1_files.length;
    },
    R2_num() {
      const R2_files = this.samples.map((el) => el.R2_file);
      return R2_files.length;
    },
  },
  methods: {
    deleteSample(sample) {
      this.$store.commit("deleteSample", sample);
    },
  },
};
</script>

<style scoped>
th,
td {
  padding: 5px;
}
</style>
