<template>
  <div class="container">
    <table border="1">
      <thead>
        <tr>
          <th>Item</th>
          <th>Number</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Projects</td>
          <td>{{ projects.length }}</td>
        </tr>
        <tr>
          <td>Study</td>
          <td>{{ study_names.length }}</td>
        </tr>
        <tr>
          <td>Raw data</td>
          <td>{{ raw_data_count }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "HomeSummary",
  mounted() {
    this.$store.dispatch("getRawDataCount");
  },
  computed: {
    ...mapState(["projects", "study_names", "raw_data_count"]),
  },
};
</script>

<style scoped>
.container {
  box-sizing: border-box;
  padding: 10px;
}
table {
  width: 300px;
  height: 100px;
}
</style>
