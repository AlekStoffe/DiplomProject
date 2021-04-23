<template>
    <div class="body-wrapper">
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
                    <span>Максимальная скидка</span>
                </el-col>
                <el-col
                        style="padding: 0px"
                        :span="8"
                        v-for="item in arr"
                        :key="item"
                >
                    <el-card
                            span="8"
                            class="card-item"
                            :body-style="{ padding: '0px' }"
                            @click.native="_openIndustryPage(item)"
                    >
                        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                             class="image"/>
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                            <div>{{ item.restaurant }}</div>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
            <el-row
                    :gutter="40"
                    class="content-array"
                    style="margin: 0 auto 40px">
                <el-col class="cards-list-title">
                    <span>Есть доставка</span>
                </el-col>
                <el-col
                        style="padding: 0px"
                        :span="8"
                        v-for="item in arr"
                        :key="item"
                >
                    <el-card
                            span="8" class="card-item"
                            :body-style="{ padding: '0px' }"
                            @click.native="_openIndustryPage(item)"
                    >
                        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                             class="image"/>
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                            <div>{{ item.restaurant }}</div>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Carousel from './carousel'
    import Footer from "@/components/footer";

    export default {
        name: "body",
        components: {
            Carousel,
            Footer,
        },
        data() {
            return {
                arr: [
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
                    {
                        name: 'Yummy hamburger',
                        restaurant: 'Ресторан',
                    },
                ]
            }
        },
        methods: {
            _openIndustryPage() {
                this.$router.push('/industry');
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
</style>