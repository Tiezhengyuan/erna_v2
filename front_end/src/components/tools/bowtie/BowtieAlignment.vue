<template>
  <div class="container bowtie-required">
    <inputNumber
      :data="bowtie_params.mismatches"
      :receive="receive"
    ></inputNumber>
    <inputNumber
      :data="bowtie_params.seed_length"
      :receive="receive"
    ></inputNumber>
    <inputNumber :data="bowtie_params.gaps" :receive="receive"></inputNumber>
    <inputNumber
      :data="bowtie_params.match_bonus"
      :receive="receive"
    ></inputNumber>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputNumber from "../../forms/inputNumber";

export default {
  name: "BowtieAlignment",
  components: {
    inputNumber,
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
