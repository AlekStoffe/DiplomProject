<template>
    <el-container style="height: 908px; overflow: auto">
        <div class="industries-wrapper">
            <el-row
                :gutter="40"
            >
                <el-col>
                    <el-button
                        class="add-industry-button"
                        @click="_openAddFormIndustry"
                    >Добавить профиль
                    </el-button>
                </el-col>
                <el-col class="cards-list-title">
                    <span>Ваши профили:</span>
                </el-col>
                <el-col
                    style="padding: 0px"
                    :span="8" v-for="profile in myProfiles" :key="profile.name"
                >
                    <el-card
                        span="8"
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        style="cursor: pointer;"
                        @click.native="_openIndustryPage(profile.id)"
                    >
                        <img
                            :src="profile.image"
                            class="image"

                        />
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold">{{ profile.name }}</div>
                            <div>{{ profile.address }}</div>
                            <div>{{ profile.description }}</div>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </el-container>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "MyIndustry",
    props: [
        'id'
    ],
    data() {
        return {
            industries: [
                {
                    name: 'Yummy hamburger',
                    restaurant: 'Ресторан',
                },
                {
                    name: 'Yummy hamburger',
                    restaurant: 'Ресторан',
                },
                {
                    name: 'Yummy hamburger',
                    restaurant: 'Ресторан',
                },
                {
                    name: 'Yummy hamburger',
                    restaurant: 'Ресторан',
                },
            ],
        };
    },
    mounted() {
        if (!localStorage.token) {
            this.$router.push('/')
        }
        this.$store.dispatch('fetchMyProfiles', { user: localStorage.userId })
        .catch(()=> this.$message({
            type: 'error',
            message: 'Ошибка получения списка профилей.',
        }))
    },
    computed: {
        ...mapState([
            'pageIsLoading',
            'myProfiles',
        ])
    },
    methods: {
        _openAddFormIndustry() {
            this.$router.push('/addIndustry');
        },

        _openIndustryPage(id) {
            this.$router.push(`/industry/${id}`);
        },
    }
}
</script>

<style lang="scss" scoped>
.industries-wrapper {
    width: 60%;
    margin: 50px auto;
}

.cards-list-title {
    font-size: 25px;
    line-height: 30px;
}

.card-item {
    height: 300px;
}

.add-industry-button {
    margin-bottom: 50px;
    padding: 20px 30px;
}
</style>