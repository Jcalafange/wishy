import { createApp } from 'vue';
import App from './App.vue';
import { createPinia } from 'pinia'
import { useAuthStore } from '@/stores/auth';
import { createVuetify } from 'vuetify';
import 'vuetify/styles';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import router from './router';

import '@mdi/font/css/materialdesignicons.css';

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
  },
});

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(vuetify);

const authStore = useAuthStore();
authStore.loadStoredData();

app.mount('#app');