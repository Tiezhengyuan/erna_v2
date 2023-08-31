import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_project from "./state/project";
import state_samples from "./state/samples";
import mutations_project from "./mutations/project";
import mutations_samples from "./mutations/samples";

export default new Vuex.Store({
  state: {
    ...state_project,
    ...state_samples,
  },
  getters: {},
  mutations: {
    ...mutations_project,
    ...mutations_samples,
  },
  actions: {},
  modules: {},
});
