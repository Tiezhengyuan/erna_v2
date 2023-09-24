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
      <inputDropdown :data="specie" :receive="receive"></inputDropdown>
      <inputDropdown :data="data_source" :receive="receive"></inputDropdown>
      <button @click="create">Create</button>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
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
  mounted() {
    this.$store.dispatch("getSpecies");
  },
  computed: {
    ...mapState(["default_project", "next_project_id", "projects"]),
    ...mapGetters(["data_source", "specie"]),
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
.new-project .project-input {
  height: 270px;
  background-color: white;
  margin: 0 auto;
  padding: 20px;
}
.new-project .title {
  font-size: 30px;
}
.new-project .project-input button {
  font-size: 18px;
  margin: 10px;
}
</style>
