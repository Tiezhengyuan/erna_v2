<template>
  <div class="container parse-samples">
    <table border="1">
      <caption>
        Parse Sample Names with Raw Files
      </caption>
      <TableTwoEnds v-if="seq_ends == 'two_ends'"></TableTwoEnds>
      <TableSingleEnd v-else></TableSingleEnd>
    </table>
  </div>
</template>

<script>
import { mapState } from "vuex";
import TableTwoEnds from "./TableTwoEnds";
import TableSingleEnd from "./TableSingleEnd";

export default {
  name: "ParseSamples",
  components: {
    TableTwoEnds,
    TableSingleEnd,
  },
  computed: {
    ...mapState(["seq_ends"]),
  },
};
</script>

<style scoped>
.parse-samples {
  width: 100%;
}
</style>
