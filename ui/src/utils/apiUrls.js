const API_VERSION = 'api'
const REACT_APP_BACKEND_URL = process.env.REACT_APP_BACKEND_URL
const HOST = `${REACT_APP_BACKEND_URL}/${API_VERSION}`

export const API_AUTH_TOKEN = `${HOST}/auth/token`
export const API_AUTH_REFRESH_TOKEN = `${HOST}/auth/token/refresh`
export const API_USER_URL = `${HOST}/profile/users/`
