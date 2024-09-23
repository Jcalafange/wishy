<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="10">
        <v-card class="elevation-6 mt-10">
          <v-window v-model="step" hide-delimiters>
            <!-- Tela de Login -->
            <v-window-item :value="1">
              <v-row>
                <v-col cols="12" md="6">
                  <v-card-text class="mt-12">
                    <h4 class="text-center">Login in to Your Account</h4>
                    <h6 class="text-center grey--text">
                      Log in to your account so you can continue building and editing your onboarding flows
                    </h6>
                    <v-row align="center" justify="center">
                      <v-col cols="12" sm="8">
                        <v-text-field
                          label="Email"
                          variant="outlined"
                          density="comfortable"
                          color="blue"
                          v-model="email"
                          class="mt-16"
                        />
                        <v-text-field
                          label="Password"
                          variant="outlined"
                          density="comfortable"
                          color="blue"
                          type="password"
                          v-model="password"
                        />
                        <v-row>
                          <v-col cols="12" sm="7">
                            <v-checkbox
                              label="Remember Me"
                              color="blue"
                              v-model="remember"
                            ></v-checkbox>
                          </v-col>
                          <v-col cols="12" sm="5">
                            <span class="caption blue--text">Forgot password</span>
                          </v-col>
                        </v-row>
                        <v-btn
                          color="blue"
                          block
                          @click="handleLogin"
                        >
                          Log in
                        </v-btn>
                        <h5 class="text-center grey--text mt-4 mb-3">
                          Or Log in using
                        </h5>
                        <div class="d-flex justify-space-between align-center mx-10 mb-16">
                          <v-btn variant="outlined" color="grey">
                            <v-icon color="red">mdi-google</v-icon>
                          </v-btn>
                          <v-btn variant="outlined" color="grey">
                            <v-icon color="blue">mdi-facebook</v-icon>
                          </v-btn>
                          <v-btn variant="outlined" color="grey">
                            <v-icon color="light-blue lighten-3">mdi-twitter</v-icon>
                          </v-btn>
                        </div>
                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-col>
                <v-col cols="12" md="6" class="blue rounded-bl-xl">
                  <div style="text-align: center; padding: 180px 0;">
                    <v-card-text class="white--text">
                      <h3 class="text-center">Don't Have an Account Yet?</h3>
                      <h6 class="text-center">
                        Let's get you all set up so you can start creating your first onboarding experience
                      </h6>
                    </v-card-text>
                    <div class="text-center">
                      <v-btn
                        variant="outlined"
                        color="white"
                        @click="step = 2"
                      >
                        SIGN UP
                      </v-btn>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-window-item>

            <!-- Tela de Cadastro -->
            <v-window-item :value="2">
              <v-row>
                <v-col cols="12" md="6" class="blue rounded-br-xl">
                  <div style="text-align: center; padding: 180px 0;">
                    <v-card-text class="white--text">
                      <h3 class="text-center">Already Signed up?</h3>
                      <h6 class="text-center">
                        Log in to your account so you can continue building and editing your onboarding flows
                      </h6>
                    </v-card-text>
                    <div class="text-center">
                      <v-btn
                        variant="outlined"
                        color="white"
                        @click="step = 1"
                      >
                        Log in
                      </v-btn>
                    </div>
                  </div>
                </v-col>

                <v-col cols="12" md="6">
                  <v-card-text class="mt-12">
                    <h4 class="text-center">Sign Up for an Account</h4>
                    <h6 class="text-center grey--text">
                      Let's get you all set up so you can start creating your first onboarding experience
                    </h6>
                    <v-row align="center" justify="center">
                      <v-col cols="12" sm="8">
                        <v-row>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="First Name"
                              variant="outlined"
                              density="comfortable"
                              color="blue"
                              v-model="firstName"
                              class="mt-4"
                            />
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Last Name"
                              variant="outlined"
                              density="comfortable"
                              color="blue"
                              v-model="lastName"
                              class="mt-4"
                            />
                          </v-col>
                        </v-row>
                        <v-text-field
                          label="Email"
                          variant="outlined"
                          density="comfortable"
                          color="blue"
                          v-model="email"
                        />
                        <v-text-field
                          label="Password"
                          variant="outlined"
                          density="comfortable"
                          color="blue"
                          type="password"
                          v-model="password"
                        />
                        <v-text-field
                          label="Descrição"
                          variant="outlined"
                          density="comfortable"
                          color="blue"
                          v-model="descricao"
                        />
                        <v-row>
                          <v-col cols="12" sm="7">
                            <v-checkbox
                              label="I Accept AAE"
                              color="blue"
                              v-model="acceptTerms"
                            ></v-checkbox>
                          </v-col>
                          <v-col cols="12" sm="5">
                            <span class="caption blue--text ml-n4">Terms & Conditions</span>
                          </v-col>
                        </v-row>
                        <v-btn
                          color="blue"
                          block
                          @click="handleSignUp"
                        >
                          Sign up
                        </v-btn>
                        <h5 class="text-center grey--text mt-4 mb-3">
                          Or Sign up using
                        </h5>
                        <div class="d-flex justify-space-between align-center mx-10 mb-11">
                          <v-btn variant="outlined" color="grey">
                            <v-icon color="red">mdi-google</v-icon>
                          </v-btn>
                          <v-btn variant="outlined" color="grey">
                            <v-icon color="blue">mdi-facebook</v-icon>
                          </v-btn>
                          <v-btn variant="outlined" color="grey">
                            <v-icon color="light-blue lighten-3">mdi-twitter</v-icon>
                          </v-btn>
                        </div>
                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/services/api';

export default {
  data() {
    return {
      step: 1,
      // Dados do formulário de login
      email: '',
      password: '',
      remember: false,
      // Dados do formulário de cadastro
      firstName: '',
      lastName: '',
      descricao: '',
      acceptTerms: false,
    };
  },
  methods: {
    async handleLogin() {
      try {
        const payload = {
          email: this.email,
          password: this.password,
        };
        const response = await api.post('auth/api-token-auth//', payload);
        const token = response.data.token;
        const user = response.data.user;
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
        this.$router.push('/');
      } catch (error) {
        console.error('Erro ao fazer login:', error);
        alert('Credenciais inválidas. Por favor, tente novamente.');
      }
    },
    async handleSignUp() {
      try {
        if (!this.acceptTerms) {
          alert('Você deve aceitar os termos e condições.');
          return;
        }
        const payload = {
          username: this.email,
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName,
          descricao: this.descricao,
        };
        await api.post('usuarios/', payload);
        alert('Usuário registrado com sucesso!');
        this.step = 1;
      } catch (error) {
        console.error('Erro ao registrar usuário:', error);
        alert('Erro ao registrar usuário. Por favor, tente novamente.');
      }
    },
  },
};
</script>

<style scoped>
.v-application .rounded-bl-xl {
  border-bottom-left-radius: 300px !important;
}
.v-application .rounded-br-xl {
  border-bottom-right-radius: 300px !important;
}
</style>
