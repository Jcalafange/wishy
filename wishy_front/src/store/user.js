import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    usuario: null
  }),
  actions: {
    login(credenciais) {
      if (credenciais.email === 'user@example.com' && credenciais.senha === '1234') {
        this.usuario = { nome: 'Usuário Exemplo', email: credenciais.email }
      } else {
        throw new Error('Credenciais inválidas')
      }
    }
  }
})