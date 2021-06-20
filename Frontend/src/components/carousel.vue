<template>
    <div class="carousel-wrapper">
        <div style="text-align: center; padding-top: 20px">
            <img src="../assets/Daco_820723.png" style="width: 250px; height: 200px; padding-bottom: 30px">
            <h2 class="carousel-title">Лишнюю еду и отходы превратим в доходы!!!</h2>
        </div>
        <el-button
                class="goToMaps"
                type="success"
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
        height: 320px;
        border-radius: 20px;
        margin: 50px auto;
        background-color: cadetblue;
    }

    .carousel-title {
        color: aliceblue;
        font-family: "Consolas";
        font-size: 26px;
    }

    .goToMaps {
        position: absolute;
        left: 437px;
        bottom: 80px;
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