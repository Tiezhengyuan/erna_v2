<template>
  <div class="container build-ref">
    <h3>Download genome references</h3>
    <label>Note: genome DNA and transcripts</label>
    <div>
      <inputDropdown :data="data_source" :receive="receive"></inputDropdown>
      <inputDropdown :data="new_specie" :receive="receive"></inputDropdown>
    </div>
    <div>
      <button @click="submit">submit download request</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "BuildReference",
  components: {
    inputDropdown,
  },
  computed: {
    ...mapGetters(["data_source", "new_specie"]),
  },
  methods: {
    receive(key_val) {
      this.$store.commit("updateNewGenome", key_val);
    },
    submit() {
      this.$store.dispatch("requestNewGenome");
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
