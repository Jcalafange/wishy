<template>
  <nav>
    <div class="nav-wrapper">
      <div class="logo">
        <router-link to="/">Wishy</router-link>
      </div>
      <ul class="nav-links">
        <li v-if="user">
          Bem-vindo, {{ user }}
        </li>
        <li v-else>
          <router-link to="/login">Login</router-link>
        </li>
        <li v-if="user">
          <a href="#" @click.prevent="logout">Sair</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      user: null,
    };
  },
  created() {
    this.user = localStorage.getItem('user');
  },
  methods: {
    logout() {
      localStorage.removeItem('user');
      this.user = null;
      this.$router.push('/login');
    },
  },
  watch: {
    // Observa mudanças na rota para atualizar o usuário
    $route() {
      this.user = localStorage.getItem('user');
    },
  },
};
</script>

<style scoped>
.nav-wrapper {
  display: flex;
  justify-content: space-between;
  background-color: #f35621;
  padding: 10px 20px;
}
.logo a {
  color: #fff;
  font-size: 24px;
  text-decoration: none;
}
.nav-links {
  list-style: none;
  display: flex;
  align-items: center;
}
.nav-links li {
  margin-left: 20px;
}
.nav-links a {
  color: #fff;
  text-decoration: none;
}
</style>
