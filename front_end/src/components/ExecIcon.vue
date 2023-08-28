<template>
  <div class="exec-icon" :style="{backgroundColor: bg_color}" @click="execTask">
    {{ display_label }}
  </div>
</template>

<script>
export default {
  name: "ExecIcon",
  props: ["task", "receive"],
  data() {
    return {
      is_exec: this.task.status == "running" ? true : false,
    }
  },
  computed: {
    bg_color() {
      return this.is_exec ? "red" : "lightgreen";
    },
    display_label() {
      return this.is_exec ? "S" : "R";
    },
  },
  methods: {
    execTask() {
      this.is_exec = ! this.is_exec;
      this.receive(this.is_exec);
      console.log(this.is_exec)
    },
  },
};
</script>

<style>
.exec-icon {
  height: 30px;
  width: 30px;
  margin: 3px;
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 6px;
  background-color: lightgreen;
}
</style>
