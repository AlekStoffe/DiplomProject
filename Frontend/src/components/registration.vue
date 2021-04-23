<template>
    <div class="registration-wrapper">
        <div class="registration-title">
            Регистрация
        </div>
        <div class="login-form-wrapper">
            <el-form
                    ref="form"
            >
                <el-form-item>
                    <el-input
                            placeholder="Имя"
                            size="50px"
                            v-model="registry.login"
                            clearable
                    />
                </el-form-item>
                <el-form-item>
                    <el-input
                            placeholder="Почта"
                            size="50px"
                            v-model="registry.email"
                            clearable
                    />
                </el-form-item>
                <el-form-item>
                    <el-input
                            placeholder="Пароль"
                            v-model="registry.password"
                            show-password
                    />
                </el-form-item>
                <el-form :inline="true">
                    <el-form-item>
                        <el-button type="primary">Регистрация</el-button>
                    </el-form-item>
                </el-form>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Registration",
        data() {
            return {
                registry: {
                    name: '',
                    email: '',
                    password: '',
                },
            };
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