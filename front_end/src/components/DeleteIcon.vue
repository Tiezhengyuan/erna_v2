<template>
  <div class="delete-icon" @click="handler">X</div>
</template>

<script>
export default {
  name: "DeleteIcon",
  props: ["delete"],
  methods: {
    handler() {
      this.delete();
    },
  },
};
</script>

<style>
.delete-icon {
  height: 30px;
  width: 30px;
  margin: 3px;
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 6px;
  background-color: red;
}
</style>
