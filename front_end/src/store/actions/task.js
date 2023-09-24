const actions_task = {
  getProjectTasks(context, project_id) {
    api.get("/task/", ).then((res) => {
      console.log(res);
    }).catch((err) => {
      console.log(err);
    });
  },

};

export default actions_task;