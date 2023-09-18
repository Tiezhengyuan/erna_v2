<template>
  <div class="container">
    <taskMethod
      :is="current_task.component"
      v-if="!!current_task.component"
    ></taskMethod>
  </div>
</template>

<script>
import { mapState } from "vuex";
import AlignerBowtie from "../../components/tools/bowtie/AlignerBowtie";
import AlignerTophat from "../../components/tools/AlignerTophat";
import AssemblerCufflinks from "../../components/tools/AssemblerCufflinks";
import CountReads from "../../components/tools/CountReads";
import TrimSeq from "../../components/tools/TrimSeq";

export default {
  name: "RNAseqRight",
  components: {
    AlignerBowtie,
    AlignerTophat,
    AssemblerCufflinks,
    CountReads,
    TrimSeq,
  },
  computed: {
    ...mapState(["current_task"]),
  },
};
</script>

<style scoped>
.container {
  width: 48%;
  background-color: white;
  border: 1px slid black;
}
</style>
