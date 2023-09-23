import axios from "axios";

export default async ( url, method, options = {}) => axios({
  url,
  method: method.toUpperCase(),
  ...options,
});