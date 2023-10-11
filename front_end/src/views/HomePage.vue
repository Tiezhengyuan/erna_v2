<template>
  <div class="container home">
    <h3 class="stat-title" @click="changeShowAsync">
      Asynchronized Tasks
      <span v-show="showAsync">
        <img src="../../node_modules/bootstrap-icons/icons/box-arrow-in-up.svg" alt="#"/>
      </span>
      <span v-show="!showAsync">
        <img src="../../node_modules/bootstrap-icons/icons/box-arrow-down.svg" alt="#"/>
      </span>
    </h3>
    <AsyncTasks class="stat" v-if="showAsync"></AsyncTasks>

    <h3 class="stat-title" @click="changeShowProcessing">
      Monitor Processing Status
      <span v-show="showProcessing">
        <img src="../../node_modules/bootstrap-icons/icons/box-arrow-in-up.svg" alt="#"/>
      </span>
      <span v-show="!showProcessing">
        <img src="../../node_modules/bootstrap-icons/icons/box-arrow-down.svg" alt="#"/>
      </span>
    </h3>
    <ProcessingStatus class="stat" v-if="showProcessing"></ProcessingStatus>
    
    <h3 class="stat-title" @click="changeShowSummary">
      Summary of eRNA
      <span v-show="showSummary">
        <img src="../../node_modules/bootstrap-icons/icons/box-arrow-in-up.svg" alt="#"/>
      </span>
      <span v-show="!showSummary">
        <img src="../../node_modules/bootstrap-icons/icons/box-arrow-down.svg" alt="#"/>
      </span>
    </h3>
    <HomeSummary class="stat" v-if="showSummary"></HomeSummary>
  </div>
</template>

<script>
import HomeSummary from "./home/HomeSummary";
import ProcessingStatus from "./home/ProcessingStatus";
import AsyncTasks from "./home/AsyncTasks";

export default {
  name: "HomePage",
  components: {
    HomeSummary,
    ProcessingStatus,
    AsyncTasks,
  },
  data() {
    return {
      showAsync: false,
      showProcessing: false,
      showSummary: false,
    };
  },
  methods: {
    changeShowAsync() {
      this.showAsync = !this.showAsync;
    },
    changeShowProcessing() {
      this.showProcessing = !this.showProcessing;
    },
    changeShowSummary() {
      this.showSummary = !this.showSummary;
    },
  },
};
</script>

<style scoped>
.home .stat-title {
  background-color: lightgoldenrodyellow;
  margin-top: 10px;
  margin-bottom: 0;
}
.home .stat {
  background-color: white;
}
.stat-title img {
  width: 25px;
  height: 25px;
}
</style>
