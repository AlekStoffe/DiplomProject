import Vue from 'vue';
import Vuex from 'vuex';
import axios from "axios";

Vue.use(Vuex)

const state = {
    user: null,
    pageIsLoading: false,
    foodType1List: [],
    foodType2List: [],
    foodType3List: [],
    mapCompanies: [],
    myProfiles: [],
    industryDataPage: {},
    cartItems: [],
    userOrders: [],
    companiesOrders: [],
    userOrderFood: [],
    companyOrderFood: [],
    selectedFood: [],
    profileComments: [],
    avgScore: 0,
    giveAwayRefuseItems: [],
    giveRefuseItems: [],
};

export default new Vuex.Store({
    state,
    mutations: {
        setPageIsLoading(state, value) {
            state.pageIsLoading = value;
        },
        setUser(state, {value} = {}) {
            state.user = value;
        },
        setFoodTypeList1(state, value) {
            state.foodType1List = value;
        },
        setFoodTypeList2(state, value) {
            state.foodType2List = value;
        },
        setFoodTypeList3(state, value) {
            state.foodType3List = value;
        },
        setMapCompanies(state, value) {
            state.mapCompanies = value;
        },
        setMyProfiles(state, value) {
            state.myProfiles = value;
        },
        setIndustryDataPage(state, value) {
            state.industryDataPage = value[0];
        },
        setCartItems(state, value) {
            state.cartItems = value;
        },
        setUserOrders(state, value) {
            state.userOrders = value;
        },
        setCompaniesOrders(state, value) {
            state.companiesOrders = value;
        },
        setUserOrderFood(state, value) {
            state.userOrderFood = value;
        },
        setCompanyOrderFood(state, value) {
            state.companyOrderFood = value;
        },
        setSelectedFood(state, value) {
            state.selectedFood = value;
        },
        setProfileComments(state, value) {
            state.profileComments = value.reverse();
        },
        setAvgScore(state, value) {
            state.avgScore = value;
        },
        setGiveAwayRefuseItems(state, value) {
            state.giveAwayRefuseItems = value;
        },
        setGiveRefuseItems(state, value) {
            state.giveRefuseItems = value;
        },
    },
    actions: {
        registration({commit}, payload) {
            commit('setPageIsLoading', true);
            return axios.post('auth/users/', payload)
                .finally((response) => {
                    commit('setPageIsLoading', false)
                    return response;
                })
        },
        fetchJwtToken({commit}, payload) {
            commit('setPageIsLoading', true);
            return axios.post('auth/token/login', payload)
                .then((response) => {
                    localStorage.token = response.data.auth_token;
                })
                .catch(() => {
                    commit('setPageIsLoading', false)
                    return Promise.reject();
                });
        },
        authorization({commit}) {
            return axios.get('auth/users/me/', {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .then((response) => {
                    commit('setUser', {value: response.data})
                    localStorage.userId = response.data.id;
                })
                .catch(() => {
                    return Promise.reject();
                })
                .finally(() => commit('setPageIsLoading', false));
        },
        fetchFoodType1({commit}) {
            commit('setPageIsLoading', true);
            return axios.get('main/1')
                .then((response) => commit('setFoodTypeList1', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchFoodType2({commit}) {
            commit('setPageIsLoading', true);
            return axios.get('main/2')
                .then((response) => commit('setFoodTypeList2', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchFoodType3({commit}) {
            commit('setPageIsLoading', true);
            return axios.get('main/3')
                .then((response) => commit('setFoodTypeList3', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchMapCompanies({commit}) {
            commit('setPageIsLoading', true);
            return axios.get('company/map/')
                .then((response) => commit('setMapCompanies', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchMyProfiles({commit}, payload) {
            commit('setPageIsLoading', true);
            return axios.get('company/user/', {
                params: payload
            })
                .then((response) => {
                    commit('setMyProfiles', response.data)
                })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        createProfile({commit}, payload) {
            commit('setPageIsLoading', true);
            return axios.post('company/create/', payload)
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        createFood({commit}, payload) {
            commit('setPageIsLoading', true);
            return axios.post('food/create/', payload)
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchIndustryPage({commit}, payload) {
            commit('setPageIsLoading', true);
            return axios.get('company/', {
                params: payload,
            })
                .then((response) => commit('setIndustryDataPage', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchCardItems({commit}, payload) {
            commit('setPageIsLoading', true)
            return axios.get(`cart/${payload}`, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .then((response) => commit('setCartItems', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        addFood({commit}, payload) {
            commit('setPageIsLoading', true)
            return axios.post('cart/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        updateQuantityCardItem({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.put('cart/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        confirmOrder({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('cart/confirmation/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(()=> {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', true))
        },
        clearCard({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('cart/delete/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchUserOrders({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.get('order/me/', {
                params: payload,
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .then((response) => commit('setUserOrders', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchCompaniesOrders({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.get('company/order/', {
                params: payload,
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .then((response) => commit('setCompaniesOrders', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchUserOrderFood({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('order/me/id/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .then((response) => commit('setUserOrderFood', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchCompanyOrderFood({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('company/order/id/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .then((response) => commit('setCompanyOrderFood', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchSelectedFood({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.get('food/', {
                params: payload,
            })
                .then((response) => commit('setSelectedFood', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        searchFood({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.get('company/map/search/', {
                params: payload,
            })
                .then((response) => commit('setMapCompanies', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        cancelCompanyOrder({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('company/order/cancel/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        confirmCompanyOrder({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('company/order/confirm/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchProfileComments({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.get('company/comment/', {
                params: payload,
            })
                .then((response) => commit('setProfileComments', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        addComment({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('comment/create/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                },
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchAvgScore({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('company/avgscore/', payload
            )
                .then((response) => commit('setAvgScore', response.data.score__avg))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchGiveAwayRefuseItems({ commit }) {
            commit('setPageIsLoading', true)
            return axios.get('trash/')
                .then((response) => commit('setGiveAwayRefuseItems', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        fetchGiveRefuseItems({ commit }) {
            commit('setPageIsLoading', true)
            return axios.get('trash/give/')
                .then((response) => commit('setGiveRefuseItems', response.data))
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        createGiveAwayRefuseItem({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('trash/create/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                }
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
        createGiveRefuseItem({ commit }, payload) {
            commit('setPageIsLoading', true)
            return axios.post('trash/give/create/', payload, {
                headers: {
                    Authorization: 'Token ' + localStorage.token,
                }
            })
                .catch(() => {
                    return Promise.reject()
                })
                .finally(() => commit('setPageIsLoading', false))
        },
    },
})