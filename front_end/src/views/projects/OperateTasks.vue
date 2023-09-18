<template>
  <div class="container-operate">
    <button @click="submitTask">Submitt Tasks</button>
    <button @click="refreshProjectTasks">Refresh Project</button>
  </div>
</template>

<script>
export default {
  name: "OperateTasks",
  methods: {
    submitTask() {
      console.log("tasks");
    },
    // remove unsubmitted tasks and get latest tasks
    refreshProjectTasks() {
      this.$store.commit("refreshProjectTasks");
    },
  },
};
</script>

<style scoped>
.container-operate {
  height: 100px;
  width: 250px;
  margin: 5px;
  padding: 5px;
  box-sizing: border-box;
  background-color: lightblue;
}
.container-operate button {
  width: 100px;
  height: 80px;
  margin: 5px;
  border-radius: 10px;
}
</style>
