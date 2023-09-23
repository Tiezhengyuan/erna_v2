<template>
  <div class="container create-project">
    <ProjectNav></ProjectNav>
    <NewProject></NewProject>
    <ListProjects></ListProjects>
  </div>
</template>

<script>
import NewProject from "./NewProject";
import ListProjects from "./ListProjects";
import ProjectNav from "./ProjectNav";

export default {
  name: "UpdateProjects",
  components: {
    ProjectNav,
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
