<template>
  <div class="container list-projects">
    <table border="1">
      <thead>
        <tr>
          <th>Project ID</th>
          <th>Project Name</th>
          <th>Description</th>
          <th>Sequencing</th>
          <th>Status</th>
          <th>Delete</th>
          <th>Edit</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(project, i) in projects" :key="i">
          <td>{{ project.project_id }}</td>
          <td>{{ project.project_name }}</td>
          <td>{{ project.description }}</td>
          <td>{{ project.sequencing }}</td>
          <td>{{ project.status }}</td>
          <td>
            <button @click="deleteProject(project)">Delete</button>
          </td>
          <td>
            <button @click="editProject(project)">Edit</button>
          </td>
        </tr>
      </tbody>
    </table>
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
    deleteProject(project) {
      const selected = project.id;
      if (this.deleted.indexOf(selected) == -1) {
        this.deleted.push(selected);
        this.$store.commit("updateDeleted", selected);
      }
    },
    editProject(project) {
      this.$store.commit("setCurrentProject", project);
    },
  },
};
</script>

<style scoped>
.container.list-projects {
  border-top: 1px solid white;
  padding: 10px;
}
.container.list-projects table {
  margin: 0 auto;
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
