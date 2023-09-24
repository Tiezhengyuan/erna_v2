<template>
  <div class="container parse-samples">
    <fieldset>
      <legend>Select a project</legend>
      <div class="select-project">
        <inputDropdown
          :data="project_names"
          :receive="getProject"
        ></inputDropdown>
      </div>
    </fieldset>

    <fieldset>
      <legend>Inject raw data into project</legend>
      <div class="select-dir">select directries</div>
      <table border="1">
        <caption>
          Parse Sample Names with Raw Files
        </caption>
        <TableTwoEnds v-if="seq_ends == 'two_ends'"></TableTwoEnds>
        <TableSingleEnd v-else></TableSingleEnd>
      </table>
    </fieldset>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";
import TableTwoEnds from "./TableTwoEnds";
import TableSingleEnd from "./TableSingleEnd";

export default {
  name: "ParseSamples",
  components: {
    inputDropdown,
    TableTwoEnds,
    TableSingleEnd,
  },
  computed: {
    ...mapState(["projects", "seq_ends"]),
    project_names() {
      return {
        name: "id",
        label: "Project ID",
        value: "",
        options: this.projects.map((el) => {
          return {
            value: el.id,
            label: el.project_id,
          };
        }),
      };
    },
  },
  methods: {
    getProject(key_val) {
      console.log(key_val);
    },
  },
};
</script>

<style scoped>
.container.parse-samples {
  width: 100%;
}
.container.parse-samples fieldset {
  border-color: lightblue;
  border-radius: 5px;
  background-color: white;
}
</style>
