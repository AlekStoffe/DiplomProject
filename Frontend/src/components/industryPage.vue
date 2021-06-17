<template>
    <div
        v-loading="pageIsLoading"
        class="industry-wrapper"
    >
        <el-row
            class="industry-card-wrapper"
        >
            <el-col class="industry-card">
                <el-row>
                    <img
                        :src="industryDataPage.image"
                        class="image-avatar"
                    />
                    <el-button
                        class="comment-button"
                        type="primary"
                        @click="_openCommentsPage"
                    >
                        Оставить отзыв
                    </el-button>
                    <div>
                        <h2>{{ industryDataPage.name }}</h2>
                    </div>
                    <div>
                        <div>{{ industryDataPage.description }}</div>
                    </div>
                    <div style="margin-top: 10px">
                        <div>Телефон: 89308975754</div>
                    </div>
                    <div>
                        <div>Адрес: {{ industryDataPage.address }}</div>
                    </div>
                    <div style="display: flex;">
                        <div style="margin-right: 10px">
                            Оценка организации:
                        </div>
                        <el-rate
                            :value="avgScore"
                            disabled
                        ></el-rate>
                    </div>
                </el-row>
                <el-row class="shop-items-wrapper">
                    <el-col
                        v-for="item in industryDataPage.food"
                        :key="item.id"
                        :span="8"
                        style="margin: 0 115px 25px 0"
                    >
                        <el-card
                            class="shop-item-card"
                            @click.native="_addItemInBasket(item)"
                        >
                            <img :src="item.image"
                                 class="image"/>
                            <div style="padding: 5px;">
                                <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                                <div style="display: flex; justify-content: space-between">
                                    <div>Кол-во: {{ item.quantity }}</div>
                                    <div class="price-wrapper">
                                        <div>{{ item.price }} Руб</div>
                                        <div style="text-decoration: line-through">{{ item.old_price }} Руб</div>
                                    </div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>
            <el-col>
                <el-card
                    class="card-shop-basket-wrapper"
                    :body-style="{ height: '870px' }"
                >
                    <div class="shop-basket-wrapper">
                        <div class="shop-basket-header">
                            <div class="shop-basket-title">
                                Корзина заказов
                            </div>
                            <i
                                class="el-icon-delete"
                                style="cursor: pointer"
                                @click="_clearCard"
                            ></i>
                        </div>
                        <div v-loading="pageIsLoading">
                            <div
                                v-for="item in cartItems"
                                :key="item.id"
                                style="margin-bottom: 15px"
                            >
                                <div class="shop-basket-name-new-price">
                                    <div class="shop-basket-item-name">
                                        {{ item.food.name }}
                                    </div>
                                    <div style="width: 50px; text-align: right">
                                        {{ item.food.price }} ₽
                                    </div>
                                </div>
                                <div class="shop-basket-count-old-price">
                                    <div class="shop-basket-counter">
                                        <i
                                            class="el-icon-minus"
                                            style="margin-right: 8px; cursor: pointer"
                                            @click="_decreaseQuantityCardItem({ quantity: item.food.quantity, id: item.id })"
                                        ></i>
                                        <i style="margin-right: 8px">{{ item.quantity }}</i>
                                        <i
                                            class="el-icon-plus"
                                            style="cursor: pointer"
                                            @click="_expandQuantityCardItem({ quantity: item.food.quantity, id: item.id })"
                                        ></i>
                                    </div>
<!--                                    <div class="shop-basket-old-price">{{ item.old_price }} ₽</div>-->
                                </div>
                            </div>
                        </div>
                        <div class="confirm-order">
<!--                            <div style="margin-bottom: 5px">-->
<!--                                Итоговая стоимость: {{ }}-->
<!--                            </div>-->
                            <el-button
                                style="width: 100%"
                                @click="_confirmOrder"
                            >Подтвердить заказ
                            </el-button>
                        </div>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "IndustryPage",
    props: [
        'id',
    ],
    data() {
        return {
            formModel: {
                adress: '',
                phone: '',
            },
        };
    },
    computed: {
        ...mapState([
            'pageIsLoading',
            'industryDataPage',
            'cartItems',
            'avgScore',
        ]),
    },
    mounted() {
        this._fetchIndustryPage();
        this._fetchAvgScore()

        if (localStorage.token) {
            this._fetchCardItems();
        }
    },
    methods: {
        _fetchIndustryPage() {
            console.log(this.id)
            this.$store.dispatch('fetchIndustryPage', {id: this.id})
        },

        _fetchCardItems() {
            this.$store.dispatch('fetchCardItems', this.id)
        },

        _addItemInBasket(item) {
            this.$store.dispatch('addFood', {food: item.id})
                .then(() => this._fetchCardItems())
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка добавления товара в корзину',
                }))
        },

        _decreaseQuantityCardItem(params) {
            console.log(params)
            this.$store.dispatch('updateQuantityCardItem', {id: params.id, quantity: -1})
                .then(() => this._fetchCardItems())
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка получения товаров в корзине',
                }))
        },

        _expandQuantityCardItem(params) {
            this.$store.dispatch('updateQuantityCardItem', {id: params.id, quantity: 1})
                .then(() => this._fetchCardItems())
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка получения товаров в корзине',
                }))
        },

        _clearCard() {
            this.$store.dispatch('clearCard', { id: this.cartItems[0].cart })
                .then(() => this._fetchCardItems())
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка очистки корзины',
                }))
        },

        _confirmOrder() {
            this.$store.dispatch('confirmOrder', {company: this.industryDataPage.food[0].company})
                .then(() => this._fetchCardItems())
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка регистрации заказа',
                }))
        },

        _openCommentsPage() {
            this.$router.push(`/comments/${this.id}`);
        },

        _fetchAvgScore() {
            this.$store.dispatch('fetchAvgScore', { company: this.id })
            .catch(() => {
                this.$message({
                    type: 'error',
                    message: 'Ошибка получения общей оценки.'
                })
            })
        }
    }
}
</script>

<style scoped lang="scss">
.industry-wrapper {
    width: 60%;
    height: 908px;
    margin: 0 auto;
}

.image-avatar {
    height: 300px;
    width: 100%;
}

.industry-card-wrapper {
    display: flex;
}

.industry-card {
    width: 1800px;
}

.card-shop-basket-wrapper {
    position: fixed;
    width: 400px;
    height: 100%;
}

.shop-basket-wrapper {
    margin: 0 10px;
    height: 100%;
}

.shop-basket-header {
    display: flex;
    margin: 25px auto;
    padding-bottom: 25px;
    font-size: 20px;
    font-weight: bold;
    color: #2c3e50;
    border-bottom: 1px solid #959597;
}

.shop-basket-title {
    margin-right: 150px;
}

.shop-basket-item-name {
    width: 300px;
    margin-right: 5px;
}

.shop-basket-name-new-price {
    display: flex;
    font-weight: bolder;
    color: #2c3e50;
    font-size: 14px;
}

.shop-basket-counter {
    display: flex;
    margin-top: 5px;
    width: 70px;
    margin-right: 235px;
    color: #2c3e50;
    font-size: 14px;
}

.shop-basket-count-old-price {
    display: flex;
    font-size: 14px;
}

.shop-basket-old-price {
    text-decoration: line-through;
}

.shop-items-wrapper {
    width: 100%;
    margin-top: 30px;
}

.shop-item-card {
    cursor: pointer;
    width: 325px;
    height: 250px;
}

.image {
    height: 150px;
}

.confirm-order {
    position: absolute;
    width: 340px;
    top: 830px;
}

.comment-button {
    position: absolute;
    z-index: 2;
    top: 230px;
    right: 30px
}
</style>