<template>
  <div class="container update-projects">
    <div class="apply-changes">
      <button @click="applyChanges">Apply all changes</button>
      <!-- {{ deleted_projects }} -->
      <!-- {{ updated_projects }} -->
    </div>
    <EditProject v-if="showUpdate"></EditProject>
    <ListProjects></ListProjects>
  </div>
</template>

<script>
import { mapState } from "vuex";
import EditProject from "./EditProject";
import ListProjects from "./ListProjects";

export default {
  name: "UpdateProjects",
  components: {
    EditProject,
    ListProjects,
  },
  computed: {
    ...mapState(["current_project", "deleted_projects", "updated_projects"]),
    showUpdate() {
      return Object.keys(this.current_project).length === 0 ? false : true;
    },
  },
  methods: {
    applyChanges() {
      if (this.deleted_projects) {
        this.$store.dispatch("deleteProjects");
      }
      if (this.updated_projects) {
        this.$store.dispatch("updateProjects");
      }
    },
  },
};
</script>

<style scoped>
.container.update-projects {
  border: 1px solid white;
}
.container.update-projects .apply-changes button {
  font-size: 24px;
  margin: 10px;
  padding: 5px;
  color: white;
  background-color: red;
}
</style>
