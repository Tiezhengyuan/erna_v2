export default {
  // set
  setGenomes(state, data) {
    state.genomes = data;
  },

  // update
  updateNewGenome(state, key_val) {
    state.new_genome[key_val[0]] = key_val[1];
  },
};
