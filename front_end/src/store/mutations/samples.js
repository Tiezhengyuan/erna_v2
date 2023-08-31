const mutations_samples = {
  deleteSample(state, sample) {
    state.samples = state.samples.filter((el) => {
      const is_sample =
        el.sample_name == sample.sample_name && el.R1_file == sample.R1_file;
      return is_sample ? 0 : 1;
    });
  },
};

export default mutations_samples;
