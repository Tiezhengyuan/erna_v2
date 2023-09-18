<template>
  <div class="container-project">
    <div class="container-label">I. Select Project</div>
    <select class="container-select" v-model="selected" @change="selectProject">
      <option v-for="(value, i) of projects" :key="i">
        {{ value }}
      </option>
    </select>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SelectProject",
  props: ["receive"],
  data() {
    return {
      selected: "",
    };
  },
  computed: {
    ...mapState(["projects"]),
  },
  methods: {
    selectProject() {
      this.$store.commit("selectProject", this.selected);
    },
  },
};
</script>

<style scoped>
.container-project {
  height: 100px;
  width: 200px;
  margin: 5px;
  padding: 5px;
  box-sizing: border-box;
  background-color: lightblue;
}
.container-label {
  margin: 10px;
}
</style>
