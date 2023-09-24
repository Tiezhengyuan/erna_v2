<template>
  <div class="container select-ref">
    <h3>Download genome references</h3>
    <label>Note: genome DNA and transcripts</label>
    <div>
      <inputDropdown
        :data="references.data_source"
        :receive="getDataSource"
      ></inputDropdown>
      <inputDropdown
        :data="references.specie"
        :receive="getSpecie"
      ></inputDropdown>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "SelectReference",
  components: {
    inputDropdown,
  },
  computed: {
    ...mapState(["references"]),
  },
  methods: {
    getDataSource(key_val) {
      console.log(key_val);
    },
    getSpecie(key_val) {
      console.log(key_val);
    },
  },
};
</script>

<style scoped>
.container.select-ref {
  background-color: white;
}
</style>
