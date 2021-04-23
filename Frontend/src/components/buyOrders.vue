<template>
    <div class="orders-wrapper">
        <div class="orders-title">
            Ваши заказы
        </div>
        <div class="orders-form-wrapper">
            <el-form
                    ref="form"
            >
                <el-form-item v-if="messageIsVisible">
                    <span>Список ваших заказов пуст!</span>
                </el-form-item>
                <el-table
                        v-if="!messageIsVisible"
                        :data="tableData"
                        width="100%"
                >
                    <el-table-column
                            fixed
                            prop="name"
                            label="Название товара"
                            min-width="100px"
                    />
                    <el-table-column
                            fixed
                            prop="restaraunt"
                            label="Ресторан"
                            min-width="200px"
                    />
                    <el-table-column
                            fixed
                            prop="delivery"
                            label="Доставка"
                            min-width="40px"
                    />
                    <el-table-column
                            fixed
                            prop="count"
                            label="Количество"
                    />
                </el-table>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "BuyOrders",
        data() {
            return {
                tableData: [
                    {
                        name: 'Продукт',
                        restaraunt: 'МакДональдс',
                        delivery: 'Да',
                        count: '2',
                    },
                    {
                        name: 'Продукт',
                        restaraunt: 'МакДональдс',
                        delivery: 'Да',
                        count: '2',
                    },
                    {
                        name: 'Продукт',
                        restaraunt: 'МакДональдс',
                        delivery: 'Да',
                        count: '2',
                    },
                    {
                        name: 'Продукт',
                        restaraunt: 'МакДональдс',
                        delivery: 'Да',
                        count: '2',
                    },
                    {
                        name: 'Продукт',
                        restaraunt: 'МакДональдс',
                        delivery: 'Да',
                        count: '2',
                    },
                    {
                        name: 'Продукт',
                        restaraunt: 'МакДональдс',
                        delivery: 'Да',
                        count: '2',
                    },
                ]
            };
        },
        computed: {
            messageIsVisible() {
                return this.tableData.length === 0;
            },
        },
    }
</script>

<style lang="scss">
    .orders-wrapper {
        width: 80%;
        overflow: auto;
        margin: 100px auto;
        text-align: center;
    }

    .orders-form-wrapper {
        width: 100%;
        margin: 0 auto;
    }

    .orders-title {
        font-size: 30px;
        margin-bottom: 20px;
    }
</style>