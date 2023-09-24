<template>
  <div class="container build-ref">
    <h3>Download genome references</h3>
    <label>Note: genome DNA and transcripts</label>
    <div>
      <inputDropdown
        :data="default_ref.data_source"
        :receive="getDataSource"
      ></inputDropdown>
      <inputDropdown
        :data="default_ref.specie"
        :receive="getSpecie"
      ></inputDropdown>
    </div>
    <div>
      <button>submit download request</button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown";

export default {
  name: "BuildReference",
  components: {
    inputDropdown,
  },
  computed: {
    ...mapState(["default_ref"]),
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
.container.build-ref {
  background-color: white;
}
</style>
