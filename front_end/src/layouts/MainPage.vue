<template>
  <div>
    <HeaderBar></HeaderBar>
    <ContentPage></ContentPage>
  </div>
</template>

<script>
import HeaderBar from "./HeaderBar";
import ContentPage from "./ContentPage";

export default {
  name: "MainPage",
  components: {
    HeaderBar,
    ContentPage,
  },
};
</script>

<style></style>
