<template>
  <div class="container">
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
.container {
  padding: 5px;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
}
.container .name {
  padding-right: 10px;
  display: flex;
  justify-content: right;
}
</style>
