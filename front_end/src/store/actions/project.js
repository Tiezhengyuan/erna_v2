// import axios from "axios";

import { api } from "./api";

const actions_project = {
  getProjects(context) {
    api.get("/project").then((res) => {
      context.commit("setUserProjects", res.data);
      context.commit("setNewProject");
    });
  },
  deleteProjects(context) {
    for (let id of context.state.deleted_projects) {
      api
        .delete(`/project/${id}/`)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    }
    context.state.deleted_projects = [];
  },
  updateProjects(context) {
    for (let id of Object.keys(context.state.updated_projects)) {
      const updated = context.state.updated_projects[id];
      api
        .put(`/project/${id}/`, updated)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    }
    context.state.updated_projects = {};
  },
  postNewProject(context) {
    // console.log(context.state.new_project);
    api
      .post("/project/", context.state.new_project)
      .then((res) => {
        context.dispatch("postReference", res.data.id);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

export default actions_project;
