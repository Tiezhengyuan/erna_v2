<template>
  <div class="container list-projects">
    <h3>Projects owned by you</h3>
    <table border="1">
      <thead>
        <tr>
          <th>Project ID</th>
          <th>Project Name</th>
          <th>Project Description</th>
          <th>Status</th>
          <th>Delate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(project, i) in projects" :key="i">
          <td>{{ project.project_id }}</td>
          <td>{{ project.project_name }}</td>
          <td>{{ project.description }}</td>
          <td>{{ project.status ? "Active" : "No" }}</td>
          <td>
            <button @click="deleteProject(project.project_id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="delete-project">
      <button @click="applyDeletion">Apply Deletion</button>
      <label v-if="!!deleted.length">{{ deleted }}</label>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "ListProjects",
  computed: {
    ...mapState(["projects"]),
  },
  data() {
    return {
      deleted: [],
    };
  },
  methods: {
    deleteProject(selected) {
      if (this.deleted.indexOf(selected) == -1) {
        this.deleted.push(selected);
        this.$store.commit("deleteProject", selected);
      }
    },
    applyDeletion() {
      this.$store.dispatch("postDeleteProjects", this.deleted);
      this.deleted = [];
    },
  },
};
</script>

<style scoped>
.container.list-projects {
  border: 1px solid white;
  padding: 10px;
}
.container .delete-project {
  margin: 20px;
}
.container .delete-project button {
  font-size: 25px;
  width: 200px;
  height: 50px;
  background-color: red;
  margin-right: 20px;
}
</style>
