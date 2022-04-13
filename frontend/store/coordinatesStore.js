import { latLng } from 'geojson'

/**
 * Nuxt Point module: coordinatesStore to handle creation of new Point
 */
export const state = () => ({
  // newPointCoord: {
  //   lat: { type: Number, default: null },
  //   lng: { type: Number, default: null },
  //   default: null,
  // },
  newPointCoord: { type: latLng, default: null },
  newLineCoord: [],
})

export const mutations = {
  /**
   * Mutation: apply newPointCoord value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {JSON object} contains object with latitude and longitude data
   */
  addPointCoord(state, data) {
    state.newPointCoord = data
  },
  /**
   * Mutation: apply newLineCoord value change to state of current store module
   *
   * @param {state} state of this store module
   * @param {JSON object} contains object with Line coordinates data (latitude and longitude)
   */
  addLineCoord(state, data) {
    state.newLineCoord = data
  },
}

export const getters = {
  /**
   * Getter for newPointCoord state values
   *
   * @param {state} state of this store module
   * @return {JSON object} object with latitude and longitude data
   */
  newPointCoord(state) {
    return state.newPointCoord
  },
  /**
   * Getter for newLineCoord state values
   *
   * @param {state} state of this store module
   * @return {JSON object} object with Line coordinates data (latitude and longitude)
   */
  newLineCoord(state) {
    return state.newLineCoord
  },
}
