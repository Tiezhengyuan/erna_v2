<template>
  <div class="container select-project">
    <slot></slot>
    <label>{{ select_label }}</label>
    <select class="container-select" v-model="selected" @change="selectProject">
      <option v-for="(project, i) of projects" :key="i" :value="project">
        {{ project.project_id }}: {{ project.project_name }}
      </option>
    </select>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SelectProject",
  props: ["select_label", "receive"],
  data() {
    return {
      selected: {},
    };
  },
  computed: {
    ...mapState(["projects"]),
  },
  methods: {
    selectProject() {
      // console.log(this.selected);
      this.$store.commit("selectProject", this.selected);
    },
  },
  updated() {
    console.log(this.selected);
    this.$store.dispatch("getProjectTasks", this.selected.project_id);
  },
};
</script>

<style scoped></style>
