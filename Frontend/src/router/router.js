import Vue from 'vue'
import VueRouter from "vue-router";
import Autorization from '../components/authorization.vue';
import Registration from '../components/registration.vue';
import Body from '../components/mainPage.vue';
import Map from '../components/map.vue';
import BuyOrders from '../components/myOrders/myOrders.vue';
import ShareFood from '../components/shareFood.vue';
import MyIndustry from '../components/myIndustry.vue';
import AddIndustry from '../components/addProfile.vue';
import IndustryPage from '../components/industryPage.vue';
import FindFood from '../components/findFood.vue';
import CommentsPage from '../components/commentsPage.vue';

Vue.use(VueRouter)

export default new VueRouter ({
    mode: 'history',
    routes: [
        { path: '/login', component: Autorization },
        { path: '/registration', component: Registration },
        { path: '/', component: Body },
        { path: '/map', component: Map },
        { path: '/orders', component: BuyOrders },
        { path: '/shareFood', component: ShareFood },
        { path: '/industries', component: MyIndustry },
        { path: '/addIndustry', component: AddIndustry },
        { path: '/industry/:id', component: IndustryPage, props: true },
        { path: '/findFood', component: FindFood },
        { path: '/comments/:id', component: CommentsPage, props: true },
    ]
})