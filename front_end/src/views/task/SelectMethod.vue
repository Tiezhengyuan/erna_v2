<template>
  <div class="container select-method">
    <slot></slot>
    <select v-model="selected">
      <option v-for="(method, i) of task_methods" :key="i" :value="i">
        {{ method.task_method }}
      </option>
    </select>
    <div class="add-task">
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
.container.select-method {
  display: block;
}
.add-task {
  margin-top: 5px;
}
</style>
