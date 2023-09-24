<template>
  <div class="task-container">
    <div>Task: {{ task.task_id }}</div>
    <div class="task-header">
      <label>{{ status }}</label>
      <button id="task-delete" @click="deleteTask">X</button>
      <button id="task-stop" @click="stopTask">||</button>
      <button id="task-submit" @click="submitTask">></button>
    </div>
    <TaskRelations :task="task"></TaskRelations>
    <div class="task-method">
      <button @click="selectTaskMethod">
        <label>Set method:</label>
        {{ task.task_method }}
      </button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import TaskRelations from "./TaskRelations";

export default {
  name: "NewTask",
  props: ["task"],
  components: {
    TaskRelations,
  },
  data() {
    return {
      status: this.task.status,
    };
  },
  computed: {
    ...mapState(["task_methods", "tasks"]),
  },
  methods: {
    deleteTask() {
      this.$store.commit("deleteTask", this.task);
    },
    submitTask() {
      this.status = "pending";
      const obj = {
        task_id: this.task.task_id,
        status: this.status,
      };
      this.$store.commit("updateTaskStatus", obj);
    },
    stopTask() {
      this.status = "stopped";
      const obj = {
        task_id: this.task.task_id,
        status: this.status,
      };
      this.$store.commit("updateTaskStatus", obj);
    },
    selectTaskMethod() {
      this.$store.commit("selectTask", this.task);
    },
  },
};
</script>

<style scoped>
.task-container {
  height: 150px;
  width: 250px;
  border-radius: 10px;
  box-sizing: border-box;
  margin: 10px;
  padding: 5px;
  background-color: lightblue;
}
.task-header {
  border: 1px solid black;
  background-color: white;
  /* height: 50px; */
  margin: 0;
  padding: 5px;
  overflow: hidden;
}
.task-header label {
  float: left;
  padding: 3px;
}
.task-header button {
  float: right;
  margin-left: 5px;
}
#task-delete {
  background-color: red;
}
#task-stop {
  background-color: orange;
}
#task-submit {
  background-color: lightgreen;
}
.task-method {
  margin: 10px;
}
</style>
