<template>
  <div class="container">
    <RNAseqHeader></RNAseqHeader>
    <div class="pipeline-container">
      <RNAseqLeft></RNAseqLeft>
      <RNAseqRight></RNAseqRight>
    </div>
  </div>
</template>

<script>
import RNAseqHeader from "./rnaseq/RNAseqHeader";
import RNAseqLeft from "./rnaseq/RNAseqLeft";
import RNAseqRight from "./rnaseq/RNAseqRight";

export default {
  name: "RNAseqPipeline",
  components: {
    RNAseqHeader,
    RNAseqLeft,
    RNAseqRight,
  },
};
</script>

<style scoped>
.pipeline-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  box-sizing: border-box;
}
</style>
