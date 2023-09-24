import { api } from "./api";

const actions_reference = {
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
  postReference(context, id) {
    const data = {
      project: id,
      specie: context.state.new_project.specie,
      data_source: context.state.new_project.data_source,
    };
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

export default actions_reference;
