<template>
  <div class="container load-samples">
    <fieldset>
      <legend>Load samples into database</legend>
      <div class="import-samples">
        <div>
          <inputText :data="study_name" :receive="setStudyName"></inputText>
          <SelectFile></SelectFile>
        </div>
        <div>
          <button @click="saveSamples">Save Samples</button>
        </div>
      </div>
      <TableSample></TableSample>
    </fieldset>

    <fieldset class="parse-samples">
      <legend>Parse raw data with samples</legend>
      <ParseSamples></ParseSamples>
    </fieldset>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import inputText from "../../components/forms/inputText";
import SelectFile from "../../components/forms/SelectFile";
import ParseSamples from "./ParseSamples";
import TableSample from "./TableSample";

export default {
  name: "LoadSamples",
  components: {
    inputText,
    SelectFile,
    TableSample,
    ParseSamples,
  },
  mounted() {
    this.$store.dispatch("getStudyNames");
  },
  computed: {
    ...mapState(["loaded_samples", "new_study_name"]),
    ...mapGetters(["study_name"]),
  },
  methods: {
    setStudyName(key_val) {
      this.$store.commit("setNewStudyName", key_val[1]);
    },
    saveSamples() {
      if (this.new_study_name && this.loaded_samples.length > 0) {
        this.$store.dispatch("postLoadedSamples");
      } else {
        console.log("study name or samples should not be empty.")
      }
    },
  },
};
</script>

<style scoped>
.container.load-samples {
  width: 100%;
}
.container.load-samples fieldset {
  border-color: lightblue;
  border-radius: 5px;
  background-color: white;
}
.import-samples {
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid grey;
}
.import-samples button {
  font-size: 20px;
  font-weight: bold;
  padding: 10px;
}
</style>
