<template>
  <div class="container">
    <RNAseqLeft></RNAseqLeft>
    <div class="pipeline-container">
      <RNAseqContent></RNAseqContent>
      <RNAseqRight></RNAseqRight>
    </div>
  </div>
</template>

<script>
import RNAseqLeft from "./rnaseq/RNAseqLeft";
import RNAseqContent from "./rnaseq/RNAseqContent";
import RNAseqRight from "./rnaseq/RNAseqRight";

export default {
  name: "RNAseqPipeline",
  components: {
    RNAseqLeft,
    RNAseqContent,
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
