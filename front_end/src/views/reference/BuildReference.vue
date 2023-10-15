<template>
  <div class="container build-ref">
    <h3>Download genome references</h3>
    <label>Note: genome DNA and transcripts</label>
    <div>
      <!-- specie -->
      <inputDropdown :data="specie_group" :receive="selectGroup"></inputDropdown>
      <inputDropdown v-show="showSpecie" :data="specie" :receive="receive"></inputDropdown>
      <!-- genome -->
      <inputDropdown :data="data_source" :receive="selectDataSource"></inputDropdown>
      <inputDropdown v-show="showVersion" :data="version" :receive="receive"></inputDropdown>
    </div>
    <div>
      <button @click="submit">Submit download request</button>
      <button @click="reset">Reset</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "BuildReference",
  mounted(){
    this.$store.dispatch("getDataSources");
    this.$store.dispatch("getSpecieGroups");
  },
  components: {
    inputDropdown,
  },
  data() {
    return {
      showSpecie: false,
      showVersion: false,
    };
  },
  computed: {
    ...mapGetters(["data_source", "specie_group",  "specie", "version"]),
  },
  methods: {
    selectGroup(key_val) {
      this.$store.commit("updateNewGenome", key_val);
      this.$store.dispatch("getSpecies");
      this.showSpecie = true;
    },
    receive(key_val) {
      this.$store.commit("updateNewGenome", key_val);
    },
    selectDataSource(key_val) {
      this.$store.commit("updateNewGenome", key_val);
      this.$store.dispatch("getVersions");
      this.showVersion = true;
    },
    submit() {
      this.$store.dispatch("requestNewGenome");
      window.location.reload();
    },
    reset() {
      window.location.reload();
    },
  },
};
</script>

<style scoped>
.container.build-ref {
  background-color: white;
}
</style>
