<template>
  <div class="container-left">
    <SelectProject :projects="projects" :receive="getProject"></SelectProject>
    <SelectMethod
      :seq_methods="seq_methods"
      :receive="getMethod"
    ></SelectMethod>
    <div>
      <button @click="addTask">Add task</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import SelectProject from "./projects/SelectProject";
import SelectMethod from "./projects/SelectMethod";

export default {
  name: "RNAseqLeft",
  components: {
    SelectProject,
    SelectMethod,
  },
  data() {
    return {
      project: "",
      seq_method: "",
    };
  },
  computed: {
    ...mapState(["projects", "seq_methods"]),
  },
  methods: {
    getProject(project) {
      this.project = project;
      console.log(this.project);
    },
    getMethod(seq_method) {
      this.seq_method = seq_method;
      console.log(this.seq_method);
    },
    addTask() {
      console.log(this.project);
      console.log(this.seq_method);
    },
  },
};
</script>

<style scoped>
.container-left {
  width: 15%;
  background-color: white;
  border: 1px slid black;
  display: block;
}
div button {
  margin-top: 20px;
}
</style>
