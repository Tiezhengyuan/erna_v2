<template>
  <div class="container new-project">
    <h3>Create a new project</h3>
    <div class="project-input" v-if="showInput">
      <PairedLabel :data="new_project_id"></PairedLabel>
      <inputText :data="project_name" :receive="receive"></inputText>
      <inputText :data="description" :receive="receive"></inputText>
      <inputDropdown :data="sequencing" :receive="receive"></inputDropdown>
      <inputDropdown :data="status" :receive="receive"></inputDropdown>
      <inputDropdown :data="ready_genome" :receive="receive"></inputDropdown>
      <button @click="create">Create</button>
      <button @click="reset">Reset</button>
    </div>
    <div class="warning" v-show="showWarning">
      Either Sequencing or genome should be selected.
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
    this.$store.dispatch("getGenomes");
    this.$store.dispatch("getNextProjectID");
  },
  data() {
    return {
      showInput: true,
      showWarning: false,
    };
  },
  computed: {
    ...mapState(["updated_project"]),
    ...mapGetters([
      "new_project_id",
      "project_name",
      "description",
      "sequencing",
      "status",
      "ready_genome",
    ]),
  },
  methods: {
    receive(key_val) {
      this.$store.commit("updateUpdatedProject", key_val);
    },
    create() {
      if (this.updated_project.sequencing && this.updated_project.genome) {
        this.$store.dispatch("postNewProject");
      } else {
        this.showWarning = true;
      }
    },
    reset() {
      window.location.reload();
    },
  },
};
</script>

<style scopred>
/* .container.new-project {
  margin: 0 auto;
} */
.new-project .project-input {
  width: 500px;
  height: 300px;
  margin: 0 auto;
  background-color: white;
  padding: 20px;
}
.new-project .title {
  font-size: 30px;
}
.new-project .project-input button {
  font-size: 18px;
  margin: 10px;
}
.new-project .warning {
  width: 500px;
  margin-top: 10px;
  color: white;
  background-color: red;
}
</style>
