export function setUserData(state, payload) {
  Object.keys(payload).forEach(key => {
    if (state.hasOwnProperty(key)) {
      state[key] = payload[key]
    }
  })
}
