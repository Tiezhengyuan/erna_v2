import { api } from "./api";

export default {
  getSpecies(context) {
    api
      .get("./specie/")
      .then((res) => {
        context.commit("setSpecies", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getGenomes(context) {
    api
      .get("./genome/")
      .then((res) => {
        context.commit("setGenomes", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  postReference(context, data) {
    api
      .post("/reference/", data)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
