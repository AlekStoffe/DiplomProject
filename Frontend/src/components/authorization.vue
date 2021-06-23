<template>
  <div
      class="authorization-wrapper"
      v-loading="pageIsLoading"
  >
    <div class="authorization-title">
      Вход
    </div>
    <div class="login-form-wrapper">
      <el-form ref="form">
        <el-form-item>
          <el-input
              placeholder="Почта"
              size="50px"
              v-model="formModel.username"
          />
        </el-form-item>
        <el-form-item>
          <el-input
              placeholder="Пароль"
              v-model="formModel.password"
              show-password
          />
        </el-form-item>
        <el-form-item v-if="this.authMessageIsVisible">
                    <span class="authorization-message">
                        Вы ввели неверный логин или пароль. Пожалуйста повторите попытку.
                    </span>
        </el-form-item>
        <el-form :inline="true">
          <el-form-item>
            <el-button
                type="primary"
                @click="_fetchJWTtoken"
            >
              Войти
            </el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="_openRegistration">Регистрация</el-button>
          </el-form-item>
        </el-form>
      </el-form>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: "Autorization",
  data() {
    return {
      formModel: {
        username: '',
        password: '',
      },
      authMock: {
        login: 'Stas',
        password: 'qweqwe',
      },
      authMessageIsVisible: false,
    };
  },
  computed: {
    ...mapState([
      'token',
      'user',
      'pageIsLoading',
    ]),
  },
  methods: {
    _openRegistration() {
      this.$router.push('/registration');
    },
    _fetchJWTtoken() {
      return this.$store.dispatch('fetchJwtToken', this.formModel)
          .then(() => this._authorization())
          .catch(() => {
            this.$message({
              type: 'error',
              message: 'Ошибка! Проверьте правильность введенных данных.',
            })
          })
    },
    _authorization() {
      return this.$store.dispatch('authorization')
          .then(() => {
            this.$message({
              type: 'success',
              message: 'Вы успешно авторизовались!',
            })
            this.$router.push('/')
          })
          .catch(() => this.$message({
            type: 'error',
            message: 'Ошибка авторизации!',
          }))
    }
  },
}
</script>

<style lang="scss" scoped>
.authorization-wrapper {
  width: 50%;
  margin: 100px auto;
  text-align: center;
}

.login-form-wrapper {
  width: 400px;
  margin: 0 auto;
}

.authorization-title {
  font-size: 30px;
  margin-bottom: 20px;
}

.authorization-message {
  line-height: 20px;
  color: red;
}
</style>