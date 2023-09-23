const mutations_user = {
  setCurrentUser(state, user) {
    state.current_user = {
      username: user.username,
      groups: user.groups,
      id: user.id,
      email: user.email,
    };
  },
};

export default mutations_user;
