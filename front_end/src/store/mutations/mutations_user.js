export default {
  setCurrentUser(state, user) {
    state.current_user = {
      username: user.username,
      groups: user.groups,
      id: user.id,
      email: user.email,
    };
  },
};
