<template>
  <div class="container project-nav">
    <button @click="create">Create</button>
    <button @click="create">Apply</button>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "ProjectNav",
  computed: {
    ...mapState["new_project"],
  },
  methods: {
    create() {
      this.$store.commit("addNewProject");
      // this.$store.dispatch("postNewProject", this.new_project);
    },
  },
};
</script>

<style scoped>
.container.project-nav {
  border-bottom: 2px solid lightblue;
}
.container.project-nav button {
  padding: 5px;
  margin: 10px;
  font-size: 20px;
  border-radius: 5px;
}
</style>
