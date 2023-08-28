<template>
  <div class="container">
    <table border="1">
      <caption>
        Monitor Processing Status
      </caption>
      <thead>
        <tr>
          <th>Project</th>
          <th>Progress</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, i) in status" :key="i">
          <td>{{ item.project }}</td>
          <td>
            <progress min="0" max="100" :value="item.progress"></progress>
          </td>
          <td>{{ item.status }}</td>
          <td>
            <button @click="runProject(item)">{{ item.label }}</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "HomeStatus",
  data() {
    return {
      status: [
        { project: "a", progress: 40, status: "running", label: "stop" },
        { project: "b", progress: 0, status: "pending", label: "stop" },
        { project: "c", progress: 100, status: "done", label: "restart" },
        { project: "d", progress: 0, status: "failed", label: "restart" },
      ],
    };
  },
  methods: {
    runProject(item) {
      if (item.label == "stop") {
        item.status = "stopped";
        item.label = "restart";
      } else {
        item.status = "pending";
        item.label = "stop";
      }
      console.log(item.project);
    },
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
  /* height: 200px; */
  border-collapse: collapse;
}
caption {
  font-weight: bold;
  margin: 5px;
}
td,
th {
  border: 2px solid #777;
  padding: 5px;
}
td progress {
  width: 80%;
  height: 30px;
  text-align: center;
}
td progress:after {
  content: attr(value) "%";
}
</style>
