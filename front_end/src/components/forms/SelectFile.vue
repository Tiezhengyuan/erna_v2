<template>
  <div class="container select-file">
    <label class="file-label">Select a file</label>
    <input
      class="file-selector"
      type="file"
      ref="myFiles"
      @change="handleFile"
    />
    {{ file }}
  </div>
</template>

<script>
export default {
  name: "SelectFile",
  data() {
    return {
      file: "",
    };
  },
  methods: {
    handleFile(e) {
      this.file = this.$refs.myFiles.files;
      console.log(this.file);
      console.log(e.target.files);
    },
  },
};
</script>

<style>
.container.select-file {
  width: 600px;
  display: flex;
}
.container.select-file .file-selector {
  margin-left: 10px;
  margin-bottom: 20px;
}
</style>
