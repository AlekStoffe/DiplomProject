<template>
    <div
        v-loading="pageIsLoading"
        class="body-wrapper"
    >
        <div class="body-content">
            <el-row>
                <el-col class="carousel">
                    <Carousel/>
                </el-col>
            </el-row>
            <el-row
                :gutter="40"
                class="content-array"
                style="margin: 0 auto 40px"
            >
                <el-col class="cards-list-title">
                    <span>Кулинария</span>
                </el-col>
                <el-col
                    style="padding: 0px"
                    :span="8"
                    v-for="item in foodType1List"
                    :key="item.name"
                >
                    <el-card
                        span="8"
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        @click.native="_openIndustryPage(item.company.id)"
                    >
                        <img :src="item.image"
                             class="image"/>
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold; font-size: 18px">{{ item.name }}</div>
                            <div style="display: flex; justify-content: space-between">
                                <div>
                                    {{ item.company.name }}
                                </div>
                                <div style="font-size: 14px; font-weight: bold">
                                    {{ item.price }} Руб
                                </div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
                <el-button
                    class="show-more-button"
                    @click="_openFindFoodPage"
                >
                    Посмотреть еще
                </el-button>
            </el-row>
            <el-row
                :gutter="40"
                class="content-array"
                style="margin: 0 auto 40px"
            >
                <el-col class="cards-list-title">
                    <span>Рыба и морепродукты</span>
                </el-col>
                <el-col
                    style="padding: 0px"
                    :span="8"
                    v-for="item in foodType2List"
                    :key="item.name"
                >
                    <el-card
                        span="8"
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        @click.native="_openIndustryPage(item.company.id)"
                    >
                        <img :src="item.image"
                             class="image"/>
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold; font-size: 18px">{{ item.name }}</div>
                            <div style="display: flex; justify-content: space-between">
                                <div>
                                    {{ item.company.name }}
                                </div>
                                <div style="font-size: 14px; font-weight: bold">
                                    {{ item.price }} Руб
                                </div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
                <el-button
                    class="show-more-button"
                    @click="_openFindFoodPage"
                >
                    Посмотреть еще
                </el-button>
            </el-row>
            <el-row
                :gutter="40"
                class="content-array"
                style="margin: 0 auto 40px"
            >
                <el-col class="cards-list-title">
                    <span>Мясо и мясопродукты</span>
                </el-col>
                <el-col
                    style="padding: 0px"
                    :span="8"
                    v-for="item in foodType3List"
                    :key="item.name"
                >
                    <el-card
                        span="8"
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        @click.native="_openIndustryPage(item.company.id)"
                    >
                        <img :src="item.image"
                             class="image"/>
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold; font-size: 18px">{{ item.name }}</div>
                            <div style="display: flex; justify-content: space-between">
                                <div>
                                    {{ item.company.name }}
                                </div>
                                <div style="font-size: 14px; font-weight: bold">
                                    {{ item.price }} Руб
                                </div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
                <el-button
                    class="show-more-button"
                    @click="_openFindFoodPage"
                >
                    Посмотреть еще
                </el-button>
            </el-row>
        </div>
<!--        <MainPageFooter/>-->
    </div>
</template>

<script>
import Carousel from './carousel'
/*
import MainPageFooter from "./mainPageFooter";
*/
import {mapState} from 'vuex';

export default {
    name: "mainPage",
    components: {
        Carousel,
/*
        MainPageFooter,
*/
    },
    mounted() {
        Promise.all([
            this._fetchFoodType1(),
            this._fetchFoodType2(),
            this._fetchFoodType3(),
        ])
        .catch(() => {
            this.$message({
                type: 'error',
                message: 'Ошибка получения продуктов.',
            })
        })
        if (localStorage.token) {
            this.$store.dispatch('authorization', localStorage.token)
        }
    },
    computed: {
        ...mapState([
            'pageIsLoading',
            'foodType1List',
            'foodType2List',
            'foodType3List',
        ]),
    },
    methods: {
        _openIndustryPage(id) {
            this.$router.push(`/industry/${id}`);
        },

        _openFindFoodPage() {
            this.$router.push('/findFood');
        },

        _fetchFoodType1() {
            this.$store.dispatch('fetchFoodType1')
        },

        _fetchFoodType2() {
            this.$store.dispatch('fetchFoodType2')
        },

        _fetchFoodType3() {
            this.$store.dispatch('fetchFoodType3')
        },
    },
}
</script>

<style lang="scss" scoped>
.body-wrapper {
    overflow: auto;
    height: 908px;
    background-color: #F4B7B7;
    background-attachment: local;
}

.cards-list-title {
    color: aliceblue;
    font-size: 25px;
    line-height: 30px;
}

.body-content {
    width: 1100px;
    margin: 0 auto;
}

.content-array {
    width: 1100px;
    margin-bottom: 20px;
}

.carousel {
    height: 400px;
}

.card-item {
    height: 300px;
}

.image {
    display: block;
    width: 100%;
    height: 200px;
}

.show-more-button {
    padding: 0;
    margin: 20px 0 0 20px;
    width: 324px;
    height: 302px;
}
</style>