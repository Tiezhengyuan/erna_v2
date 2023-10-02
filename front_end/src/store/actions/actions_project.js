import { api } from "./api";

export default {
  getProjects(context) {
    api.get("/project").then((res) => {
      context.commit("setUserProjects", res.data);
      context.commit("setNewProject");
    });
  },
  getNextProjectID(context) {
    api.get("/project/next_project_id/").then((res) => {
      context.commit("setNextProjectID", res.data);
    });
  },
  deleteProjects(context) {
    for (let project_id of context.state.deleted_projects) {
      api
        .delete(`/project/${project_id}/`)
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
    for (let project_id of Object.keys(context.state.updated_projects)) {
      const updated = context.state.updated_projects[project_id];
      api
        .put(`/project/${project_id}/`, updated)
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
    const u = context.state.updated_project;
    const n = context.state.new_project;
    const project = {
      project_name: u.project_name ? u.project_name : n.project_name,
      description: u.description ? u.description : n.description,
      status: u.status ? u.status : n.status,
      sequencing: u.sequencing ? u.sequencing : n.sequencing,
    };
    api
      .post("/project/", project)
      .then((res) => {
        const reference = {
          project: res.data.project_id,
          genome: u.genome ? u.genome : n.genome,
        };
        console.log(reference);
        context.dispatch("postReference", reference);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
