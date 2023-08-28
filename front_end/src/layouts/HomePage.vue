<template>
  <div class="container">
    <HomeSummary class="summary"></HomeSummary>
    <HomeStatus class="status"></HomeStatus>
  </div>
</template>

<script>
import HomeSummary from "../components/HomeSummary";
import HomeStatus from "../components/HomeStatus";

export default {
  name: "HomePage",
  components: {
    HomeSummary,
    HomeStatus,
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-around;
}
.summary,
.status {
  height: 400px;
  width: 400px;
  background-color: white;
  overflow: auto;
}
</style>
