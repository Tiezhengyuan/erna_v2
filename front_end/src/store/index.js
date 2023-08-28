import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_project from "./state/project";

export default new Vuex.Store({
  state: {
    ...state_project,
  },
  getters: {},
  mutations: {},
  actions: {},
  modules: {},
});
