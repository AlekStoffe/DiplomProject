<template>
    <div class="orders-wrapper">
        <div class="orders-title">
            Ваши заказы
        </div>
        <el-radio-group
            v-model="orders_type"
        >
            <el-radio-button
                :label="true"
            >
                Заказали вы
            </el-radio-button>
            <el-radio-button
                :label="false"
            >
                Заказали у вас
            </el-radio-button>
        </el-radio-group>
        <div class="orders-form-wrapper">
            <user-orders v-if="orders_type"/>
            <company-orders v-else/>
        </div>
    </div>
</template>

<script>
import UserOrders from "./userOrders.vue";
import CompanyOrders from "./companyOrders.vue";

export default {
    name: "BuyOrders",
    components: {
        UserOrders,
        CompanyOrders,
    },
    data() {
        return {
            orders_type: true,
        }
    },
}
</script>

<style lang="scss">
.orders-wrapper {
    width: 80%;
    overflow: auto;
    margin: 30px auto;
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

.buttons-dialog-container {
    margin-top: 30px;
}
</style>