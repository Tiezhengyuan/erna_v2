import axios from "axios";

const method_get = {
  create() {
    axios.get("https://yesno.wtf/api").then((res) => {
      this.answer = res.data;
    });
  },
};
export default method_get;
