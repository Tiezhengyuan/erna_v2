<template>
  <div class="container input-dropdown">
    <div class="input-name" v-show="data.label">
      <label>{{ data.label }}</label>
    </div>
    <select :name="data.name" v-model="selected" @change="add">
      <option
        v-for="(item, i) of data.options"
        :key="i"
        :value="item.value"
        :selected="showSelected(item.value)"
      >
        {{ item.label }}
      </option>
    </select>
    <label class="required" v-show="data.required">*</label>
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
.container.input-dropdown {
  padding: 5px;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
}
.container.input-dropdown .input-name {
  /* width: 40%; */
  padding-right: 10px;
  display: flex;
  justify-content: right;
}
.container.input-dropdown .required {
  padding-left: 10px;
  font-weight: bold;
}
</style>
