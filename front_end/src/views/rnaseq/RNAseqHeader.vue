<template>
  <div class="container-left">
    <SelectProject></SelectProject>
    <div class="container-arrow">>></div>
    <SelectMethod></SelectMethod>
    <div class="container-arrow">>></div>
    <OperateTasks></OperateTasks>
  </div>
</template>

<script>
import SelectProject from "../projects/SelectProject";
import SelectMethod from "../projects/SelectMethod";
import OperateTasks from "../projects/OperateTasks";

export default {
  name: "RNAseqHeader",
  components: {
    SelectProject,
    SelectMethod,
    OperateTasks,
  },
};
</script>

<style scoped>
.container-left {
  background-color: white;
  margin-bottom: 10px;
  border: 1px slid black;
  display: flex;
}
div button {
  margin-top: 20px;
}
.container-arrow {
  height: 100px;
  width: 30px;
  margin: 5px;
  padding: 5px;
  line-height: 100px;
  box-sizing: border-box;
  background-color: lightgray;
}
</style>
