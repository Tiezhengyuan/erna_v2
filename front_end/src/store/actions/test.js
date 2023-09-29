import { test_api } from "./api";
import { smartscope_api } from "./api";

const actions_test = {
  test(context) {
    test_api.get().then((res) => {
      context.commit("setNewAnswer", res.data);
    });
  },
  getGroups() {
    smartscope_api
      .get("/groups/")
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

export default actions_test;
