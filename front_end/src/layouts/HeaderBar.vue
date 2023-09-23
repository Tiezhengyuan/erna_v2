<template>
  <div class="container">
    <div class="logo">
      <img src="#" />
    </div>
    <div>
      <h1>eRNA v2</h1>
    </div>
    <div class="login">
      User Name: <mark>{{ current_user.username }}</mark> |
      <a href="#">logout</a>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "HeaderBar",
  computed: {
    ...mapState(["current_user"]),
  },
};
</script>

<style scoped>
.container {
  height: 100px;
  background-color: lightblue;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
}
.container .logo {
  width: 100px;
  border: 1px solid white;
}
.container .login {
  text-align: right;
  margin-top: 10px;
}
a {
  margin-left: 10px;
  margin-right: 10px;
}
</style>
