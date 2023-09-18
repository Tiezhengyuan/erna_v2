const mutations_bowtie = {
  updateBowtieParams(state, key_val) {
    state.bowtie_params[key_val[0]].value = key_val[1];
    console.log(state.bowtie_params.suppress_unalign);
  },
};

export default mutations_bowtie;
