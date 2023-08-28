<template>
  <div class="container">
    <RNAseqLeft></RNAseqLeft>
    <RNAseqContent></RNAseqContent>
    <RNAseqRight></RNAseqRight>
  </div>
</template>

<script>
import RNAseqLeft from "../components/RNAseqLeft";
import RNAseqContent from "../components/RNAseqContent";
import RNAseqRight from "../components/RNAseqRight";

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
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  box-sizing: border-box;
}
</style>
