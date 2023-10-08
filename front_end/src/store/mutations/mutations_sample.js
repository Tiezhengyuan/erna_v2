export default {
  setNewStudyName(state, name) {
    state.new_study_name = name;
  },
  addStudyName(state, data) {
    state.study_names.push(data);
  },
  setLoadedSamples(state, sample_content) {
    state.loaded_samples = [];
    let names = sample_content[0].split(",");
    names = ["sample_name", ...names.slice(1)];
    state.loaded_samples.names = names;
    for (let r = 1; r < sample_content.length; r++) {
      const values = sample_content[r].split(",");
      const item = Object.fromEntries(
        names.map((name, i) => {
          return [name, values[i]];
        })
      );
      state.loaded_samples.push(item);
    }
  },
  deleteSample(state, sample) {
    state.samples = state.samples.filter((el) => {
      const is_sample =
        el.sample_name == sample.sample_name && el.R1_file == sample.R1_file;
      return is_sample ? 0 : 1;
    });
  },
  updateParseSamples(state, key_val) {
    state.parse_samples[key_val[0]] = key_val[1];
  },
  setUnparsedData(state, data) {
    data.sort((a, b) => {
      const a_name = a.sample_name.toUpperCase();
      const b_name = b.sample_name.toUpperCase();
      let cmp = 0;
      if (a_name < b_name) {
        cmp = -1;
      } else if (a_name > b_name) {
        cmp = 1;
      } else {
        const a_batch = a.batch_name.toUpperCase();
        const b_batch = b.batch_name.toUpperCase();
        if (a_batch < b_batch) {
          cmp = -1;
        } else if (a_batch > b_batch) {
          cmp = 1;
        }
      }
      return cmp;
    });
    state.unparsed_data = data;
  },
  removeUnparsedData(state, index) {
    state.unparsed_data = state.unparsed_data.filter((el,i) => {
      return index !== i;
    });
  }
};
