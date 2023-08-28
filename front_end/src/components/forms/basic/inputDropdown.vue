<template>
  <div class="container">
    <div class="name" v-show="data.label">
      <label>{{ data.label }}</label>
    </div>
    <select :name="data.name">
      <option
        v-for="(value, i) of data.options"
        :key="i"
        :selected="selected(value)"
        :value="value"
        :change="add"
      >
        {{ value }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: "inputDropdown",
  props: ["data", "receive"],
  methods: {
    selected(value) {
      return value == this.data.value ? true : false;
    },
    add(e) {
      console.log(e.target.value);
      // this.data.value = e.target.value;
      const obj = {
        [this.data.name]: this.data,
      };
      this.receive(obj);
    },
  },
};
</script>

<style scoped>
.container {
  padding: 5px;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
}
.container .name {
  width: 40%;
  padding-right: 10px;
  display: flex;
  justify-content: right;
}
</style>
