<template>
  <div class="container create-project">
    <NewProject></NewProject>
    <ListProjects></ListProjects>
  </div>
</template>

<script>
import NewProject from "./NewProject";
import ListProjects from "./ListProjects";

export default {
  name: "CreateProject",
  components: {
    NewProject,
    ListProjects,
  },
};
</script>

<style scoped>
.container.create-project {
  border: 1px solid white;
}
</style>
