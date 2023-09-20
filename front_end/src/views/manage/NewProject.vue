<template>
  <div class="container new-project">
    <h3>Create a new project</h3>
    <div class="container-input">
      <PairedLabel :data="new_project_id"></PairedLabel>
      <inputText
        :data="default_project.project_name"
        :receive="receive"
      ></inputText>
      <inputText
        :data="default_project.description"
        :receive="receive"
      ></inputText>
      <inputDropdown
        :data="default_project.seq"
        :receive="receive"
      ></inputDropdown>
      <inputBoolean
        :data="default_project.status"
        :receive="receive"
      ></inputBoolean>
    </div>
    <div class="submit-project">
      <button @click="create">Create</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import PairedLabel from "../../components/showing/PairedLabel";
import inputText from "../../components/forms/inputText";
import inputDropdown from "../../components/forms/inputDropdown";
import inputBoolean from "../../components/forms/inputBoolean";

export default {
  name: "NewProject",
  components: {
    PairedLabel,
    inputText,
    inputDropdown,
    inputBoolean,
  },
  computed: {
    ...mapState(["default_project", "new_project"]),
    new_project_id() {
      return {
        label: "Project ID: ",
        value: this.new_project.project_id,
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
