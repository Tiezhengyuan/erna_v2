<template>
  <div class="content-container">
    <div class="content-title" v-show="current_project.id">
      Project: {{ current_project.project_id }}
    </div>
    <div class="tasks-container">
      <NewTask
        v-for="(task, i) in project_tasks"
        :key="i"
        :task="task"
      ></NewTask>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import NewTask from "../task/NewTask";

export default {
  name: "RNAseqLeft",
  components: {
    NewTask,
  },
  computed: {
    ...mapState(["current_project", "tasks"]),
    project_tasks() {
      return this.tasks.filter((el) => {
        return el.project == this.current_project ? 1 : 0;
      });
    },
  },
};
</script>

<style scoped>
.content-container {
  width: 50%;
  background-color: white;
  box-sizing: border-box;
  margin-right: 10px;
  border: 1px slid black;
}
.content-title {
  font-size: 30px;
  margin: 10px;
}
.tasks-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  overflow: auto;
}
</style>
