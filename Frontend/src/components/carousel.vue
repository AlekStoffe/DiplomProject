<template>
    <div class="carousel-wrapper">
        <el-carousel trigger="click">
            <el-carousel-item
                    class="carousel-item"
                    v-for="item in items" :key="item"
            >
                <h3 class="carousel-content">{{ item }}</h3>
            </el-carousel-item>
        </el-carousel>
        <el-button
                class="goToMaps"
                type="primary"
                @click="_goToMaps"
        >
            Открыть на картах
        </el-button>
    </div>
</template>

<script>
    export default {
        name: "Carousel",
        data() {
            return{
                items: ['1', '2 ', '3', '4']
            }
        },
        methods: {
            _goToMaps() {
                this.$router.push('/map');
            },
        },
    }
</script>

<style lang="scss" scoped>
    .carousel-wrapper{
        width: 1100px;
        height: 500px;
        margin: 50px auto;
    }

    .goToMaps {
        position: absolute;
        left: 437px;
        bottom: 90px;
        z-index: 2;
        width: 230px;
    }

    .carousel-item:nth-child(2n) {
        background-color: cadetblue;
    }

    .carousel-item:nth-child(2n+1) {
        background-color: darkkhaki;
    }

    .carousel-content {
        margin-top: 130px;
        text-align: center;
    }

    .text {
        text-align: center;
    }
</style>