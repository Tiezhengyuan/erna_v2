<template>
  <div class="container input-radio">
    <div class="name">
      <label>{{ data.label }}</label>
    </div>
    <div class="value" v-for="(p, i) of data.options" :key="i">
      <input type="radio" :name="data.name" :value="p" @change="add" />{{ p }}
    </div>
  </div>
</template>

<script>
export default {
  name: "inputRadio",
  props: ["data", "receive"],
  methods: {
    add(e) {
      const obj = [this.data.name, e.target.value];
      this.receive(obj);
    },
  },
};
</script>

<style scoped>
.container.input-radio {
  padding: 5px;
  display: flex;
  flex-direction: row;
}
.container.input-radio .name {
  padding-right: 10px;
  display: flex;
  justify-content: right;
  font-weight: bold;
}
</style>
