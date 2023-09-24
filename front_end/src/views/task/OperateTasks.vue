<template>
  <div class="container operate-tasks">
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
.container.operate-tasks {
  display: flex;
  align-items: center;
}
.container.operate-tasks button {
  height: 50px;
  margin: 5px;
  border-radius: 10px;
}
</style>
