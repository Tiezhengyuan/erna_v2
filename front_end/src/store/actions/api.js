import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;

export const test_api = axios.create({
  baseURL: "https://yesno.wtf/api",
  transformResponse(res) {
    res = JSON.parse(res);
    return res;
  },
});

export const api = axios.create({
  baseURL: "http://localhost:8000/api/",
  // withCredentials: false,
  headers: {
    ContentType: "application/json",
    Accept: "application/json",
  },
  auth: {
    username: "admin",
    password: "admin",
  },
  // responseType: "json",
  // headers: {
  //   "Content-Type": null,
  // },
  transformResponse(res) {
    try {
      return JSON.parse(res);
    } catch (e) {
      return res;
    }
  },
});
