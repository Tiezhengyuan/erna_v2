import { test_api } from "./api";

const actions_test = {
  test(context) {
    test_api.get().then((res) => {
      context.commit("setNewAnswer", res.data);
    });
  },
};

export default actions_test;
