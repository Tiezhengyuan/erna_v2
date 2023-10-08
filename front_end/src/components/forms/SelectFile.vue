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
    handleFile() {
      this.file = this.$refs.myFiles.files[0];
      const reader = new FileReader();
      reader.onload = (res) => {
        const content = res.target.result.split("\n").map((el) => {
          return el.replace("\r", "");
        });
        this.$store.commit("setLoadedSamples", content);
      };
      reader.onerror = (err) => console.log(err);
      reader.readAsText(this.file);
    },
  },
};
</script>

<style>
.container.select-file {
  width: 600px;
  display: flex;
  margin-left: 20px;
}
.container.select-file .file-selector {
  margin-left: 10px;
}
</style>
