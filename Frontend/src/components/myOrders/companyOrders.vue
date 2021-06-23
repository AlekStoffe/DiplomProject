<template>
    <div class="orders-wrapper">
        <div class="orders-form-wrapper">
            <el-form
                ref="form"
            >
                <el-form-item
                    label="Тип профиля"
                    style="width: 500px"
                >
                    <el-select
                        v-model="company_type"
                        placeholder="Выберите тип предприятия"
                        style="width: 100%"
                        @change="fetchCompanyOrders"
                    >
                        <el-option
                            v-for="item in myProfiles"
                            :key="item.id"
                            :label="item.name"
                            :value="item.id"
                        />
                    </el-select>
                </el-form-item>
                <el-form-item v-if="messageIsVisible">
                    <span>Список ваших заказов пуст!</span>
                </el-form-item>
                <el-table
                    v-if="!messageIsVisible"
                    :data="companiesOrders"
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
            <el-table :data="companyOrderFood">
                <el-table-column property="food.name" label="Название" width="300"></el-table-column>
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
            <div class="buttons-dialog-container">
                <el-button
                    @click="cancelOrder"
                >
                    Отменить
                </el-button>
                <el-button
                    @click="confirmOrder"
                    type="primary"
                >
                    Подтвердить
                </el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "CompanyOrders",
    data() {
        return {
            dialogTableVisible: false,
            dialogTitle: '',
            company_type: '',
        };
    },
    mounted() {
        this.fetchMyProfiles();
    },
    computed: {
        ...mapState([
            'companiesOrders',
            'myProfiles',
            'companyOrderFood',
        ]),

        messageIsVisible() {
            return (this.companiesOrders.length === 0 || this.company_type === '');
        },
    },
    methods: {
        openDialogInfo(pk) {
            this.dialogTitle = pk;
            this.$store.dispatch('fetchCompanyOrderFood', {id: pk})
                .then(() => this.dialogTableVisible = true)
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка'
                }))
        },

        confirmOrder() {
            this.$confirm('Вы  уверены, что хотите подтвердить заказ?', {
                confirmButtonText: 'Подтвердить',
                cancelButtonText: 'Назад',
            })
                .then(() => {
                    let requestPayload = this.companyOrderFood.map(item => item = {
                        id: item.food.id,
                        quantity: item.quantity,
                        cart: item.cart,
                    })
                    this.$store.dispatch('confirmCompanyOrder', requestPayload)
                        .then(() => {
                            this.fetchCompanyOrders(this.company_type)
                            this.dialogTableVisible = false
                        })
                        .catch(() => this.$message({
                            type: 'error',
                            message: 'Ошибка подтверждения заказа'
                        }))
                })
                .catch(() => console.log('no ok'))
        },

        cancelOrder() {
            this.$confirm('Вы  уверены, что хотите отменить заказ?', {
                confirmButtonText: 'Отменить',
                cancelButtonText: 'Назад',
            })
                .then(() => {
                    this.$store.dispatch('cancelCompanyOrder', {id: this.dialogTitle})
                        .then(() => {
                            this.fetchCompanyOrders(this.company_type)
                            this.dialogTableVisible = false
                        })
                        .catch(() => this.$message({
                            type: 'error',
                            message: 'Ошибка отмены заказа'
                        }))
                })
                .catch(() => console.log('no ok'))
        },

        fetchMyProfiles() {
            this.$store.dispatch('fetchMyProfiles', {user: localStorage.userId})
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка получения списка заказов'
                }))
        },

        fetchCompanyOrders() {
            console.log(this.company_type)
            this.$store.dispatch('fetchCompaniesOrders', {company: this.company_type})
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

.buttons-dialog-container {
    margin-top: 30px;
}
</style>