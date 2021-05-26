<template>
  <div
      class="registration-wrapper"
      v-loading="pageIsLoading"
  >
    <div class="registration-title">
      Регистрация
    </div>
    <div class="login-form-wrapper">
      <el-form ref="form">
        <el-form-item>
          <el-input
              placeholder="Имя"
              size="50px"
              v-model="formModel.username"
              clearable
          />
        </el-form-item>
        <el-form-item>
          <el-input
              placeholder="Почта"
              size="50px"
              v-model="formModel.email"
              clearable
          />
        </el-form-item>
        <el-form-item>
          <el-input
              placeholder="Пароль"
              v-model="formModel.password"
              show-password
          />
        </el-form-item>
        <el-form :inline="true">
          <el-form-item>
            <el-button
                type="primary"
                @click="registry"
            >
              Регистрация
            </el-button>
          </el-form-item>
        </el-form>
      </el-form>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: "Registration",
  data() {
    return {
      formModel: {
        username: '',
        email: '',
        password: '',
      },
    };
  },
  computed: {
    ...mapState([
      'pageIsLoading',
    ]),
  },
  methods: {
    registry() {
      this.$store.dispatch('registration', this.formModel)
          .then((response) => {
            if (response.data.id) {
              this.$message({
                type: 'success',
                message: 'Подвердите регистрацию на почте и выполните вход.',
              })
              this.$router.push('./login')
            }
          })
          .catch(() => this.$message({
            type: 'error',
            message: 'Ошибка! Проверьте правильность введенных данных.',
          }))
    },
  },
}
</script>

<style lang="scss" scoped>
.registration-wrapper {
  width: 50%;
  margin: 100px auto;
  text-align: center;
}

.login-form-wrapper {
  width: 400px;
  margin: 0 auto;
}

.registration-title {
  font-size: 30px;
  margin-bottom: 20px;
}
</style>