<template>
  <div class="container rnaseq-left">
    <SelectProject class="select">
      <div class="container-label">I. Select Project</div>
    </SelectProject>
    <div class="container-arrow">>></div>
    <SelectMethod class="select">
      <div class="container-label">II: Select method</div>
    </SelectMethod>
    <div class="container-arrow">>></div>
    <OperateTasks class="select"></OperateTasks>
  </div>
</template>

<script>
import SelectProject from "../project/SelectProject";
import SelectMethod from "../task/SelectMethod";
import OperateTasks from "../task/OperateTasks";

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
.container.rnaseq-left {
  background-color: white;
  margin-bottom: 10px;
  border: 1px slid black;
  display: flex;
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
.container-label {
  margin: 10px;
}
.container .select {
  height: 90px;
  margin: 5px;
  padding: 5px;
  background-color: lightblue;
}
</style>
