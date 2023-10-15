import { api, endpoint } from "./api";

export default {
  // get
  getDataSources(context) {
    api
      .get("./genome/data_sources/")
      .then((res) => {
        context.state.data_sources = res.data.names;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getGenomes(context) {
    const config = {
      params: { is_ready: 'True' },
    };
    api
      .get("./genome/", config)
      .then((res) => {
        context.state.ready_genomes = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getSpecieGroups(context) {
    api
      .get("./specie/group_names/")
      .then((res) => {
        context.state.specie_groups = res.data.names;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getSpecies(context) {
    const config = {
      params: {
        group: context.state.new_genome.group,
      },
    };
    api
      .get("./specie/", config)
      .then((res) => {
        context.state.species = res.data.map((el) => {
          return el.organism_name;
        });
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getVersions(context) {
    const config = {
      params: {
        data_source: context.state.new_genome.data_source,
        group: context.state.new_genome.group,
        specie: context.state.new_genome.specie,
      },
    };
    api
      .get("./genome/", config)
      .then((res) => {
        context.state.versions = res.data.map((el) => {
          return el.version;
        });
      })
      .catch((err) => {
        console.log(err);
      });
  },

  // create new project
  postReference(context, data) {
    console.log(data);
    api
      .post("/reference/", data)
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((err) => {
        console.log(err);
      });
  },

  // asynchronization
  requestNewGenome(context) {
    const config = {
      params: context.state.new_genome,
    };
    endpoint
      .get("/celery_tasks/download_genome/", config)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
