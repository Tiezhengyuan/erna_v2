<template>
  <div class="container new-project">
    <h3>Create a new project</h3>
    <div class="project-input">
      <PairedLabel :data="default_project_id"></PairedLabel>
      <inputText
        :data="default_project.project_name"
        :receive="receive"
      ></inputText>
      <inputText
        :data="default_project.description"
        :receive="receive"
      ></inputText>
      <inputDropdown
        :data="default_project.sequencing"
        :receive="receive"
      ></inputDropdown>
      <inputDropdown
        :data="default_project.status"
        :receive="receive"
      ></inputDropdown>
    </div>
    <div class="project_create">
      <button @click="create">Create</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import PairedLabel from "../../components/showing/PairedLabel";
import inputText from "../../components/forms/inputText";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "CreateProject",
  components: {
    PairedLabel,
    inputText,
    inputDropdown,
  },
  computed: {
    ...mapState(["default_project", "next_project_id", "projects"]),
    default_project_id() {
      return {
        label: "Project ID: ",
        value: this.next_project_id,
      };
    },
  },
  methods: {
    receive(key_val) {
      this.$store.commit("updateNewProject", key_val);
    },
    create() {
      this.$store.commit("addNewProject");
      this.$store.dispatch("postNewProject");
      this.$store.commit("setNewProject");
    },
  },
};
</script>

<style scopred>
.project-input {
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
</style>
