<template>
  <div class="container">
    <div class="name">
      <label>{{ data.label }}</label>
    </div>
    <div class="value">
      <input
        type="number"
        :min="data.min"
        :max="data.max"
        :name="data.name"
        :value="data.value"
        @change="add"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "inputNumber",
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
