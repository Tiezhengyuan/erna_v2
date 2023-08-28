<template>
  <div class="container-method">
    <p>II: Select method</p>
    <select v-model="selected" @change="getSelected">
      <option v-for="(value, i) of seq_methods" :key="i">
        {{ value }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: "SelectMethod",
  props: ["seq_methods", "receive"],
  data() {
    return {
      selected: "",
    };
  },
  methods: {
    getSelected() {
      this.receive(this.selected);
    },
  },
};
</script>

<style scoped>
.container-method {
  height: 100px;
  background-color: white;
  border: 1px slid black;
}
.container-method p {
  padding-bottom: 10px;
}
</style>
