<template>
    <div class="orders-wrapper">
        <div class="orders-form-wrapper">
            <el-form
                ref="form"
            >
                <el-form-item v-if="messageIsVisible">
                    <span>Список ваших заказов пуст!</span>
                </el-form-item>
                <el-table
                    v-if="!messageIsVisible"
                    :data="userOrders"
                    width="100%"
                >
                    <el-table-column
                        prop="pk"
                        label="Заказ №"
                        min-width="100px"
                    />
                    <el-table-column
                        label="Стоимость">
                        <template slot-scope="props">
                            <p>
                                {{ props.row.total_price }} Руб
                            </p>
                        </template>
                    </el-table-column>
                    <el-table-column>
                        <template slot-scope="props">
                            <el-button
                                style="width: 200px"
                                @click="openDialogInfo(props.row.pk)">Посмотреть информацию
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-form>
        </div>
        <el-dialog
            :title="`Заказ №${dialogTitle}`"
            :visible.sync="dialogTableVisible"
        >
            <el-table :data="userOrderFood">
                <el-table-column property="food.name" label="Название" width="200"></el-table-column>
                <el-table-column property="quantity" label="Количество"></el-table-column>
                <el-table-column property="food.price" label="Цена"></el-table-column>
                <el-table-column label="Компания">
                    <template slot-scope="props">
                        <p>
                            {{ props.row.food.company.name }}
                        </p>
                    </template>
                </el-table-column>
            </el-table>
        </el-dialog>
    </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "UsersOrders",
    data() {
        return {
            dialogTableVisible: false,
            dialogTitle: '',
        };
    },
    mounted() {
        this.fetchUserOrders();
    },
    computed: {
        ...mapState([
            'userOrders',
            'userOrderFood',
        ]),

        messageIsVisible() {
            return this.userOrders.length === 0;
        },
    },
    methods: {
        openDialogInfo(pk) {
            this.dialogTitle = pk;
            this.$store.dispatch('fetchUserOrderFood', { id: pk })
                .then(() => this.dialogTableVisible = true)
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка'
                }))
        },

        fetchUserOrders() {
            this.$store.dispatch('fetchUserOrders', {user: localStorage.userId})
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка получения списка заказов'
                }))
        },
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
</style>