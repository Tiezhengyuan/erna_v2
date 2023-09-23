// GET
export const getHttp = async (
  url,
  params,
  options,
) => baseHttp(
  url,
  "get",
  {params, ...options},
);
 