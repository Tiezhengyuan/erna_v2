<template>
  <div class="container bowtie-required">
    <inputDropdown
      :data="bowtie_params.specie"
      :receive="receive"
    ></inputDropdown>
    <inputDropdown
      :data="bowtie_params.raw_format"
      :receive="receive"
    ></inputDropdown>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputDropdown from "../../forms/inputDropdown";

export default {
  name: "BowtieRequired",
  components: {
    inputDropdown,
  },
  computed: {
    ...mapState(["bowtie_params"]),
  },
  methods: {
    receive(key_val) {
      this.$store.commit("updateBowtieParams", key_val);
    },
  },
};
</script>

<style scoped></style>
