import Vue from "vue";
import VueRouter from "vue-router";

import HomePage from "../layouts/HomePage";
import SampleManagement from "../layouts/SampleManagement";
import RNAseqPipeline from "../layouts/RNAseqPipeline";
import AnalyticTools from "../layouts/AnalyticTools";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/sample",
    name: "sample",
    component: SampleManagement,
  },
  {
    path: "/rnaseq",
    name: "rnaseq",
    component: RNAseqPipeline,
  },
  {
    path: "/tools",
    name: "tools",
    component: AnalyticTools,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
