<template>
    <div class="authorization-wrapper">
        <div class="authorization-title">
            Вход
        </div>
        <div class="login-form-wrapper">
            <el-form
                    ref="form"
            >
                <el-form-item>
                    <el-input
                            placeholder="Почта"
                            size="50px"
                            v-model="auth.login"
                    />
                </el-form-item>
                <el-form-item>
                    <el-input
                            placeholder="Пароль"
                            v-model="auth.password"
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
                        <el-button type="primary" @click="_authorization">Войти</el-button>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="_openRegistration">Регистрация</el-button>
                    </el-form-item>
                </el-form>
                <el-button type="text">Забыли пароль или не можете войти?</el-button>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Autorization",
        data() {
            return {
                auth: {
                    login: '',
                    password: '',
                },
                authMock: {
                  login: 'Stas',
                  password: 'qweqwe',
                },
                authMessageIsVisible: false,
            };
        },
        methods: {
            _openRegistration() {
                this.$router.push('/registration');
            },
            _authorization() {
                if(this.auth.login === this.authMock.login && this.auth.password === this.authMock.password) {
                    this.$store.commit('authorizationComplete', true);
                    this.$router.push('/')
                    return;
                }
                this.authMessageIsVisible = true;
            },
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