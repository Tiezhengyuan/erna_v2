<template>
  <div class="container">
    <div class="name" v-show="data.label">
      <label>{{ data.label }}</label>
    </div>
    <select :name="data.name" v-model="selected" @change="add">
      <option
        v-for="(value, i) of data.options"
        :key="i"
        :value="value"
        :selected="showSelected(value)"
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
  data() {
    return {
      selected: this.data.value,
    };
  },
  methods: {
    showSelected(value) {
      return value == this.selected ? true : false;
    },
    add() {
      const obj = [this.data.name, this.selected];
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
  /* width: 40%; */
  padding-right: 10px;
  display: flex;
  justify-content: right;
}
</style>
