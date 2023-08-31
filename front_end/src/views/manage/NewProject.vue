<template>
  <div class="container">
    <h2>Create a new project</h2>
    <label class="title"> Project ID: {{ new_project.project_id }} </label>
    <div class="container-input">
      <inputText v-bind:data="project_name" :receive="receive"></inputText>
      <inputText v-bind:data="description" :receive="receive"></inputText>
      <inputDropdown v-bind:data="seq" :receive="receive"></inputDropdown>
      <inputBoolean v-bind:data="status" :receive="receive"></inputBoolean>
    </div>
    <div class="submit-project">
      <button @click="create">Create</button>
      <button @click="reset">Reset</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputText from "../../components/forms/inputText";
import inputDropdown from "../../components/forms/inputDropdown";
import inputBoolean from "../../components/forms/inputBoolean";

export default {
  name: "NewProject",
  components: {
    inputText,
    inputDropdown,
    inputBoolean,
  },
  data() {
    return {
      changed: {},
      original: {
        sequencing: "mRNA-Seq",
        status: true,
      },
      project_name: {
        name: "project_name",
        label: "Project Name",
        value: "",
      },
      description: {
        name: "description",
        label: "Project Description",
        value: "",
      },
      seq: {
        name: "sequencing",
        label: "Sequencing Technique",
        value: "mRNA-Seq",
        options: ["mRNA-Seq", "miRNA-Seq", "scRNA-Seq", "Other"],
      },
      status: {
        name: "status",
        label: "Project Status",
        value: true,
      },
    };
  },
  computed: {
    ...mapState(["new_project"]),
  },
  methods: {
    receive(val_obj) {
      this.changed = { ...this.changed, ...val_obj };
      // console.log(this.changed);
    },
    create() {
      this.original = { ...this.original, ...this.changed };
      this.$store.commit("updateProject", this.original);
    },
    reset() {
      this.project_name = { ...this.project_name, value: "" };
      this.description = { ...this.description, value: "" };
      this.seq = { ...this.seq, value: "mRNA-Seq" };
      this.status = { ...this.status, value: true };
    },
  },
};
</script>

<style scopred>
.container-input {
  width: 600px;
  height: 200px;
  box-sizing: border-box;
  background-color: white;
  margin: 0 auto;
  padding: 20px;
}
.title {
  font-size: 30px;
}
.submit-project {
  margin: 20px;
}
.submit-project button {
  width: 80px;
  height: 40px;
  margin: 10px;
}
</style>
