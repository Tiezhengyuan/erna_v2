const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
});
// module.exports = {
//   devServer: {
//     proxy: "http://localhost:8000",
//   },
// };
// .\chrome.exe --disable-web-security --user-data-dir="c:/ChromeDevSession"