<template>
  <div class="container paried-label">
    <div class="name">
      <label>{{ data.label }}</label>
    </div>
    <div class="value">
      <label>{{ data.value }}</label>
    </div>
  </div>
</template>

<script>
export default {
  name: "inputText",
  props: ["data"],
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
  font-weight: bold;
  padding-right: 10px;
  display: flex;
  justify-content: right;
}
</style>
