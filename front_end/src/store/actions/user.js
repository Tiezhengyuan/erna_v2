import { api } from "./api";

const actions_user = {
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

export default actions_user;
