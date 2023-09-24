<template>
  <div class="container edit-project">
    <h3>Edit project {{ current_project.project_id }}</h3>
    <div class="project-input">
      <inputText :data="project_name" :receive="receive"></inputText>
      <inputText :data="description" :receive="receive"></inputText>
      <inputDropdown :data="sequencing" :receive="receive"></inputDropdown>
      <inputDropdown :data="status" :receive="receive"></inputDropdown>
      <div class="project_create">
        <button @click="saveUpdate">save update</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputText from "../../components/forms/inputText";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "EditProject",
  components: {
    inputText,
    inputDropdown,
  },
  computed: {
    ...mapState(["current_project"]),
    project_name() {
      return {
        name: "project_name",
        label: "Project Name",
        value: this.current_project.project_name,
      };
    },
    description() {
      return {
        name: "description",
        label: "Description",
        value: this.current_project.description,
      };
    },
    sequencing() {
      return {
        name: "sequencing",
        label: "Sequencing Technique",
        value: this.current_project.sequencing,
        options: [
          { value: "M", label: "mRNA-Seq", name: "a" },
          { value: "MI", label: "miRNA-Seq", name: "a" },
          { value: "SC", label: "scRNA-Seq", name: "a" },
          { value: "O", label: "Other", name: "a" },
        ],
      };
    },
    status() {
      return {
        name: "status",
        label: "Status",
        value: this.current_project.status,
        options: [
          { value: "A", label: "active" },
          { value: "I", label: "inactive" },
        ],
      };
    },
  },
  methods: {
    receive(key_val) {
      this.$store.commit("updateCurrentProject", key_val);
    },
    saveUpdate() {
      this.$store.commit("updateUpdated");
    },
  },
};
</script>

<style scopred>
.container.edit-project {
  padding: 10px;
  border-top: 1px solid white;
}
.project-input {
  width: 400px;
  height: 180px;
  box-sizing: border-box;
  background-color: white;
  margin: 0 auto;
  padding: 20px;
}
.title {
  font-size: 30px;
}
</style>
