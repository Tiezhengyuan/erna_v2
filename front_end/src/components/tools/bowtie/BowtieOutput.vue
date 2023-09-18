<template>
  <div class="container bowtie-output">
    <inputBoolean
      :data="bowtie_params.suppress_unalign"
      :receive="receive"
    ></inputBoolean>
    <inputBoolean
      :data="bowtie_params.suppress_header"
      :receive="receive"
    ></inputBoolean>
    <inputBoolean
      :data="bowtie_params.suppress_sq_header"
      :receive="receive"
    ></inputBoolean>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputBoolean from "../../forms/inputBoolean";

export default {
  name: "BowtieOutput",
  components: {
    inputBoolean,
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
