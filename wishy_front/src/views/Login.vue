<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Nome de Usuário:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Senha:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Entrar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    handleLogin() {
      // Simulação de autenticação
      if (this.username && this.password) {
        // Salvar o nome de usuário no localStorage
        localStorage.setItem('user', this.username);
        // Redirecionar para a página inicial
        this.$router.push('/');
      } else {
        alert('Por favor, preencha todos os campos.');
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 50px auto;
}
.form-group {
  margin-bottom: 15px;
}
</style>
