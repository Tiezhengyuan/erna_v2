<template>
  <div>
    <HeaderBar></HeaderBar>
    <ContentPage></ContentPage>
    <FooterBar></FooterBar>
  </div>
</template>

<script>
import HeaderBar from "./HeaderBar";
import ContentPage from "./ContentPage";
import FooterBar from "./FooterBar";

export default {
  name: "MainPage",
  components: {
    HeaderBar,
    ContentPage,
    FooterBar,
  },
};
</script>

<style></style>
