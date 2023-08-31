<template>
  <div class="container-method">
    <div class="container-label">II: Select method</div>
    <select v-model="selected">
      <option v-for="(value, i) of seq_methods" :key="i">
        {{ value }}
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
    ...mapState(["current_project", "seq_methods", "new_task_id"]),
  },
  methods: {
    addTask() {
      this.task = {
        project: this.current_project,
        seq_method: this.selected,
        status: "new",
        task_id: this.new_task_id,
      };
      console.log(this.task);
      this.$store.commit("addTask", this.task);
      console.log(this.new_task_id);
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
