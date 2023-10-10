<template>
  <div class="container import-samples">
    <div class="operate">
      <div class="select-project">
        <label>Select a project</label>
        <inputDropdown :data="projects_list" :receive="selectProject"></inputDropdown>
      </div>
      <div>
        <label>Add samples</label>
        <inputDropdown :data="study_names" :receive="selectStudy"></inputDropdown>
        <button>Save</button>
      </div>
    </div>
    <div class="show-data" v-show="project_files.length > 0">
      <div>
        <h3>{{ current_project.project_id }}</h3>
      </div>
      <table border="1">
        <thead>
          <tr>
            <th>Study name</th>
            <th>Sample name</th>
            <th>Number of files</th>
          </tr>
        </thead>
        <tbody>
            <tr v-for="(item, i) in project_files" :key="i">
              <th>{{ item.study_name }}</th>
              <th>{{ item.sample_name }}</th>
              <th>{{ item.raw_data.length }}</th>
            </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "ImportRawData",
  components: {
    inputDropdown,
  },
  computed: {
    ...mapState(["current_project"]),
    ...mapGetters(["projects_list", "study_names", "project_files"]),
  },
  methods: {
    selectProject(key_val) {
      this.$store.commit("setCurrentProject", key_val);
      this.$store.dispatch("getCurrentProjectFiles");
    },
    selectStudy(key_val) {
      const study_name = key_val[1]
      this.$store.dispatch("getUnassignedSampleFiles", study_name);
    },
  },
};
</script>

<style scoped>
.container.import-samples {
  display: flex;
}
.import-samples .select-project {
  border-bottom: 1px solid black;
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.import-samples button {
  font-size: 20px;
  font-weight: bold;
  margin: 5px;
  width: 80px;
}
.import-samples .operate {
  width: 250px;
  border-color: lightblue;
  border-radius: 5px;
  background-color: white;
  padding: 10px;
  margin-right: 10px;
}
.import-samples .show-data {
  width: 600px;
  border-color: lightblue;
  border-radius: 5px;
  background-color: white;
  padding: 10px;
}
</style>
