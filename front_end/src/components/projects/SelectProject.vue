<template>
  <div class="container-project">
    <p>I: Select project</p>
    <select v-model="selected" @change="selectProject">
      <option v-for="(value, i) of projects" :key="i">
        {{ value }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: "SelectProject",
  props: ["projects", "receive"],
  data() {
    return {
      selected: "",
    };
  },
  methods: {
    selectProject() {
      this.receive(this.selected);
    },
  },
};
</script>

<style scoped>
.container-project {
  height: 100px;
  background-color: white;
  border: 1px slid black;
}
.container-project p {
  padding-bottom: 10px;
}
</style>
