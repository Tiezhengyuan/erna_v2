import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import HomePage from "../views/HomePage";
import SampleManagement from "../views/SampleManagement";
import RNAseqPipeline from "../views/RNAseqPipeline";
import AnalyticTools from "../views/AnalyticTools";

import CreateProject from "../views/manage/CreateProject";
import EditProject from "../views/manage/EditProject";
import ParseSamples from "../views/manage/ParseSamples";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/manage",
    name: "manage",
    component: SampleManagement,
    children: [
      {
        path: "create_project",
        name: "create_project",
        component: CreateProject,
      },
      {
        path: "edit_project",
        name: "edit_project",
        component: EditProject,
      },
      {
        path: "parse_samples",
        name: "parse_samples",
        component: ParseSamples,
      },
    ],
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
