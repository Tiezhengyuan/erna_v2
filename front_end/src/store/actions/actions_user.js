import { api } from "./api";

export default {
  getCurrentUser(context) {
    api
      .get("/user/current/")
      .then((res) => {
        context.commit("setCurrentUser", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
