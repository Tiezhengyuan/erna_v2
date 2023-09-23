// import axios from "axios";

import { api } from "./api";

const actions_project = {
  getProjects(context) {
    api.get("/project").then((res) => {
      context.commit("setUserProjects", res.data);
      context.commit("setNewProject");
    });
  },
  deleteProjects(context, deleted_ids) {
    for (let id of deleted_ids) {
      api
        .delete(`/project/${id}/`)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  postNewProject(context) {
    // console.log(context.state.new_project);
    api
      .post("/project/", context.state.new_project)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

export default actions_project;
