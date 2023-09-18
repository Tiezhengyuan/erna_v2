import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_project from "./state/project";
import state_samples from "./state/samples";
import state_bowite from "./state/bowtie";
import mutations_project from "./mutations/project";
import mutations_samples from "./mutations/samples";
import mutations_bowtie from "./mutations/bowtie";

export default new Vuex.Store({
  state: {
    ...state_project,
    ...state_samples,
    ...state_bowite,
  },
  getters: {},
  mutations: {
    ...mutations_project,
    ...mutations_samples,
    ...mutations_bowtie,
  },
  actions: {},
  modules: {},
});
