import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
});

api.interceptors.request.use(
    (config) => {
      const token = localStorage.getItem('token');
      if (token) {
        config.headers.Authorization = `Token ${token}`; // ou `Bearer ${token}`, dependendo da sua API
      }
      return config;
    },
    (error) => Promise.reject(error)
  );

export default api;