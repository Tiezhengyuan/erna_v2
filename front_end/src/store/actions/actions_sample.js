import { api } from "./api";

export default {
  getProjectSamples(context, project_id) {
    api
      .get(`/project_sample/${project_id}`)
      .then((res) => {
        context.state.project_samples = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getStudyNames(context) {
    api
      .get("/sample/study_names/")
      .then((res) => {
        context.state.study_names = res.data.study_names;
        context.state.study_name = "";
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getStudyFiles(context, study_name) {
    const config = {
      params: {study_name: study_name},
    };
    api
      .get("/sample_file/study_files/", config)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getUnassignedSampleFiles(context, study_name) {
    const config = {
      params: {
        project_id: context.state.current_project.project_id,
        study_name: study_name
      },
    };
    api
      .get("/sample_project/unassigned_sample_files/", config)
      .then((res) => {
        context.state.current_study_name = study_name;
        context.state.unassigned_sample_files = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  postLoadedSamples(context) {
    const data = context.state.loaded_samples.map((el) => {
      let meta = Object.assign({}, el);
      delete meta.sample_name;
      return {
        study_name: context.state.new_study_name,
        sample_name: el.sample_name,
        metadata: meta,
      };
    });
    api
      .post("/sample/load_samples/", data)
      .then(() => {
        context.dispatch("getStudyNames");
        context.state.loaded_samples = [];
        context.state.new_study_name = "";
      })
      .catch((err) => {
        console.log(err);
      });
  },
  detectUnparsedData(context) {
    const config = {
      params: context.state.parse_samples,
    };
    console.log(config.params);
    api
      .get("/sample_file/unparsed_data/", config)
      .then((res) => {
        context.commit("setUnparsedData", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  parseSampleFiles(context) {
    const data = context.state.unparsed_data.map((el) => {
      return {
        sample: el.sample_id,
        raw_data: el.raw_data_id,
      };
    });
    api
      .post("/sample_file/parse_sample_files/", data)
      .then(() => {
        context.state.unparsed_data = [];
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
