<template>
  <div class="container">
    <div class="name">
      <label>{{ data.label }}</label>
    </div>
    <div class="value">
      <input
        type="range"
        min="0"
        max="1"
        :name="data.name"
        :value="Number(data.value)"
        @change="change"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "inputText",
  props: ["data", "receive"],
  methods: {
    change(e) {
      const obj = [this.data.name, Boolean(e.target.value)];
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
.container .value input {
  width: 50px;
}
</style>
