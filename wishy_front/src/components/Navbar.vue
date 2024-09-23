<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>MeuApp</v-toolbar-title>
    <v-spacer></v-spacer>
    <div v-if="authStore.user">
      Bem-vindo, {{ authStore.user.first_name }}
      <v-btn text @click="logout">Sair</v-btn>
    </div>
    <div v-else>
      <v-btn text @click="$router.push('/login')">Login</v-btn>
    </div>
  </v-app-bar>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const authStore = useAuthStore();

const logout = () => {
  authStore.logout();
  router.push('/login');
};
</script>
