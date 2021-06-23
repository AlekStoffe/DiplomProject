<template>
    <div>
        <el-drawer
            :visible.sync="visible"
            :size="size"
            title="Личный кабинет"
        >
            <el-row v-if="!user">
                <el-col>
                    <div class="menu-items">
                        <el-button
                            icon="el-icon-edit"
                            @click="_transitionToLogin"
                        >
                            Войти
                        </el-button>
                    </div>
                </el-col>
            </el-row>
            <el-row
                v-if="user"
                class="menu-items-wrapper"
            >
                <el-col class="menu-items">
                    <el-button
                        type="text"
                        icon="el-icon-user"
                        style="font-size: 16px"
                    >
                        {{ user.username }}
                    </el-button>
                </el-col>
                <el-col class="menu-items">
                    <el-button
                        type="text"
                        icon="el-icon-shopping-cart-2"
                        style="font-size: 16px"
                        @click="_openOrders"
                    >Мои заказы
                    </el-button>
                </el-col>
                <el-col class="menu-items">
                    <el-button
                        type="text"
                        icon="el-icon-share"
                        style="font-size: 16px"
                        @click="_openShareFood"
                    >Поделиться едой
                    </el-button>
                </el-col>
                <el-col class="menu-items">
                    <el-button
                        type="text"
                        icon="el-icon-s-shop"
                        style="font-size: 16px"
                        @click="_openMyIndustry"
                    >Профили
                    </el-button>
                </el-col>
                <el-col class="menu-items">
                    <el-button
                        type="text"
                        icon="el-icon-search"
                        style="font-size: 16px"
                        @click="_openFindFoodPage"
                    >Найти еду
                    </el-button>
                </el-col>
                <el-col class="menu-items">
                    <el-button
                        type="text"
                        icon="el-icon-delete"
                        style="font-size: 16px"
                        @click="_openRefusePage"
                    >Отходы
                    </el-button>
                </el-col>
                <el-col class="menu-items">
                    <el-button
                        class="exit-button"
                        type="text"
                        icon="el-icon-close"
                        style="font-size: 16px"
                        @click="_exit"
                    >Выйти
                    </el-button>
                </el-col>
            </el-row>
        </el-drawer>
    </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "drawer-menu",
    data() {
        return {
            visible: false,
            size: '20%',
        }
    },
    mounted() {
        if (localStorage.token) {
            this.$store.dispatch('authorization')
        }
    },
    computed: {
        ...mapState([
            'user',
        ]),
    },
    methods: {
        open() {
            this.visible = true;
        },

        _transitionToLogin() {
            this.visible = false;
            this.$router.push('/login');
        },

        _exit() {
            this.visible = false;
            if (this.$router.currentRoute.fullPath !== '/') {
                this.$router.push('/');
            }
            localStorage.removeItem('token');
            localStorage.removeItem('id');
            this.$store.commit('setUser', {value: null});
        },

        _openOrders() {
            this.visible = false;
            this.$router.push('/orders');
        },

        _openShareFood() {
            this.visible = false;
            this.$router.push('/shareFood');
        },

        _openMyIndustry() {
            this.visible = false;
            this.$router.push('/industries');
        },

        _openFindFoodPage() {
            this.visible = false;
            this.$router.push('/findFood');
        },

        _openRefusePage() {
            this.visible = false;
            this.$router.push('/refuse');
        }
    },
}
</script>

<style lang="scss" scoped>
.el-drawer .el-drawer__header {
    margin-left: 20px;
}

.el-drawer__close-btn {
    margin-right: 18px;
}

.menu-items {
    margin-left: 20px;
    font-size: 16px;
}

.menu-items-wrapper {
    overflow: hidden;
    margin-top: 20px;
}

.exit-button {
    margin-top: 550px;
}
</style>