<template>
  <div class="container parse-samples">
    <div class="select">
      <inputDropdown :data="study_names" :receive="receive"></inputDropdown>
      <inputText :data="sample_name_reg" :receive="receive"></inputText>
      <button @click="parseSampleFiles">Submit</button>
    </div>

    <table border="1" v-show="unparsed_data.length">
      <thead>
        <tr>
          <th>Delete</th>
          <th>Sample name</th>
          <th>Batch of raw data</th>
          <th>File path of raw data</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, i) in unparsed_data" :key="i">
          <th>
            <button @click="removeFile(i)">delete</button>
          </th>
          <th>{{ item.sample_name }}</th>
          <th>{{ item.batch_name }}</th>
          <th>{{ item.full_path }}</th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";
import inputText from "../../components/forms/inputText";

export default {
  name: "ParseSamples",
  components: {
    inputDropdown,
    inputText,
  },
  computed: {
    ...mapState(["unparsed_data"]),
    ...mapGetters(["study_names", "sample_name_reg"]),
  },
  methods: {
    receive(key_val) {
      this.$store.commit("updateParseSamples", key_val);
      this.$store.dispatch("detectUnparsedData");
    },
    removeFile(i) {
      // i is index of unparsed_data
      this.$store.commit("removeUnparsedData", i);
    },
    parseSampleFiles() {
      this.$store.dispatch("parseSampleFiles");
    },
  },
};
</script>

<style scoped>
.container.parse-samples {
  width: 100%;
}
.container.parse-samples fieldset {
  border-color: lightblue;
  border-radius: 5px;
  background-color: white;
}
.container.parse-samples .select {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
