import { api } from "./api";

export default {
  // getProjectTasks(context, project_id) {
  //   api.get("/task/", ).then((res) => {
  //     console.log(res);
  //   }).catch((err) => {
  //     console.log(err);
  //   });
  // },
  getCeleryTasks(context, status="ALL") {
    const config = {
      params: { status: status },
    };
    api
      .get("/celery_task_result/", config)
      .then((res) => {
        context.state.celery_tasks = res.data.map((el) => {
          el.task_name = String(el.task_name).replace("celery_tasks.tasks.", "");
          el.date_created = el.date_created.split(".")[0];
          el.date_done = el.date_done.split(".")[0];
          return el;
        });
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
