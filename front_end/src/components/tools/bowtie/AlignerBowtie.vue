<template>
  <div class="container bowtie">
    <div>
      <h3>aligner: Bowtie2</h3>
    </div>
    <fieldset class="required">
      <legend>Required parameters</legend>
      <BowtieRequired></BowtieRequired>
    </fieldset>
    <fieldset class="alignment">
      <legend>Alignment options</legend>
      <BowtieAlignment></BowtieAlignment>
    </fieldset>
    <fieldset class="output">
      <legend>Output options</legend>
      <BowtieOutput></BowtieOutput>
    </fieldset>
    <div>
      <button @click="save">Save</button>
    </div>
  </div>
</template>

<script>
import BowtieRequired from "./BowtieRequired";
import BowtieAlignment from "./BowtieAlignment";
import BowtieOutput from "./BowtieOutput";

export default {
  name: "AlignerBowtie",
  components: {
    BowtieRequired,
    BowtieAlignment,
    BowtieOutput,
  },
  methods: {
    save() {
      console.log("save Bowtie2");
    },
  },
};
</script>

<style scoped>
.container.bowtie {
  width: 500px;
  border: 1px solid black;
}
</style>
