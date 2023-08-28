<template>
  <div class="container-task">
    <div>Task: {{ task.name }}</div>
    <div class="task-header">
      <label :style="{backgroundColor: bg_color}">{{ task.status }}</label>
      <DeleteIcon class="task-button" :delete="deleteTask">X</DeleteIcon>
      <ExecIcon class="task-button" :task="task" :receive="getExec"></ExecIcon>
    </div>
    <div class="task-output">

    </div>
  </div>
</template>

<script>
import ExecIcon from "./ExecIcon";
import DeleteIcon from "./DeleteIcon";

export default {
  name: "VCPool",
  components: {
    ExecIcon,
    DeleteIcon,
  },
  props: ["task", "delete", "update"],
  computed: {
    bg_color() {
      if (this.task.status == "running") {
        return "orange";
      }else if (this.task.status == "stopped") {
        return "yellow";
      } else if (this.task.status == "done") {
        return "lightgreen";
      } else if (this.task.status == "pending") {
        return "lightgrey";
      }
      return "red";
    },
  },
  methods: {
    deleteTask() {
      console.log(this.task.name);
      this.delete(this.task.name);
    },
    getExec(is_exec) {
      this.update(this.task.name, is_exec);
    },
  },
};
</script>

<style scoped>
.container-task {
  height: 200px;
  width: 200px;
  margin: 10px;
 padding: 10px;
  box-sizing: border-box;
  background-color: white;
  border: 1px solid black;
}
.task-header {
  border: 1px solid black;
  margin: 0;
  padding: 5px;
  overflow: hidden;
}
.task-header label {
  float: left;
  padding: 3px;
  box-sizing: border-box;
}
.task-button {
  float: right;
}
</style>