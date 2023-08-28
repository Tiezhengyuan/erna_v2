<template>
  <div class="container">
    <table border="1">
      <caption>
        Summary of data analysis
      </caption>
      <thead>
        <tr>
          <th>Item</th>
          <th>Number</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(name, i) of Object.keys(summary)" :key="i">
          <td>{{ name }}</td>
          <td>{{ summary[name] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "HomeSummary",
  data() {
    return {
      summary: {
        projects: 4,
        raw_data: 120,
      },
    };
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
