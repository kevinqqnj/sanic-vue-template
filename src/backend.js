import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['JWT'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  getResource () {
    return $axios.get(`resource?id=xxx`)
      .then(response => response.data)
  },
  postResource () {
    return $axios.post(`resource`, {
      id: 'kevinqq',
      email: 'aaa@bbb.com'
    })
      .then(response => response.data)
  },
  postResourceAuthorized () {
    return $axios.post(`resource`, {
      id: 'kevinqq',
      email: 'aaa@bbb.com'
    }, {
      headers: { 'Authorization': 'Correct Token' }
    })
      .then(response => response.data)
  }
}
