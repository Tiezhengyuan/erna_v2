<template>
  <div class="container-method">
    <div class="container-label">II: Select method</div>
    <select v-model="selected">
      <option v-for="(method, i) of task_methods" :key="i" :value="i">
        {{ method.task_method }}
      </option>
    </select>
    <div>
      <button @click="addTask">Add task</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SelectMethod",
  data() {
    return {
      selected: "",
    };
  },
  computed: {
    ...mapState(["current_project", "task_methods", "new_task_id"]),
  },
  methods: {
    addTask() {
      const selected_method = this.task_methods[this.selected];
      this.task = {
        ...selected_method,
        project: this.current_project,
        status: "new",
        task_id: this.new_task_id,
        parent_task: "",
      };
      // console.log(this.task);
      this.$store.commit("addTask", this.task);
      // console.log(this.new_task_id);
    },
  },
};
</script>

<style scoped>
.container-method {
  height: 100px;
  width: 250px;
  margin: 5px;
  padding: 5px;
  box-sizing: border-box;
  background-color: lightblue;
}
.container-label {
  margin: 10px;
}
</style>
