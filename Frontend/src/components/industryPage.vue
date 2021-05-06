<template>
  <div class="industry-wrapper">
    <el-row class="industry-card-wrapper">
      <el-col class="industry-card">
        <el-row>
          <img
              :src="organization.img"
              class="image-avatar"
          />
          <div>
            <div>{{ organization.type }}</div>
          </div>
          <div>
            <div>{{ organization.name }}</div>
          </div>
          <div>
            <div>{{ organization.note }}</div>
          </div>
          <div>
            <div>Телефон: {{ organization.phone }}</div>
          </div>
          <div>
            <div>Адрес: {{ organization.adress }}</div>
          </div>
        </el-row>
        <el-row class="shop-items-wrapper">
          <el-col
              v-for="item in shopItems"
              :key="item.id"
              :span="8"
              style="margin: 0 115px 25px 0"
          >
            <el-card
                class="shop-item-card"
                @click.native="_addItemInBasket(item)"
            >
              <img :src="item.img"
                   class="image"/>
              <div style="padding: 5px;">
                <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                <div>{{ item.oldPrice }}</div>
                <div>{{ item.newPrice }}</div>
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
                  @click="_clearShopBasket"
              ></i>
            </div>
            <div
                v-for="item in shopBasketItems"
                :key="item.id"
                style="margin-bottom: 15px"
            >
              <div class="shop-basket-name-new-price">
                <div class="shop-basket-item-name">
                  {{ item.name }}
                </div>
                <div>
                  {{ item.newPrice }} ₽
                </div>
              </div>
              <div class="shop-basket-count-old-price">
                <div class="shop-basket-counter">
                  <i
                      class="el-icon-minus"
                      style="margin-right: 8px; cursor: pointer"
                  ></i>
                  <i style="margin-right: 8px">{{ item.count }}</i>
                  <i
                      class="el-icon-plus"
                      style="cursor: pointer"
                      @click="_addCount(item.id)"
                  ></i>
                </div>
                <div class="shop-basket-old-price">{{ item.oldPrice }} ₽</div>
              </div>
            </div>
            <div class="confirm-order">
              <el-button style="width: 100%">Подтвердить заказ</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "IndustryPage",
  data() {
    return {
      formModel: {
        adress: '',
        phone: '',
      },
      organization: {
        img: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        type: 'Ресторан',
        name: 'Ресторан',
        note: 'Описание фых=афызафхыщафщдыащзфыазфыащзбхф   щзбафы щзбфыаыза щзшлащзшлфы шлафыал фшыалзш фылалзш флаыз',
        phone: '8-930-898-6667',
        adress: 'Ул. фабричная 2/9',
      },
      shopBasketItems: [
        {
          id: 0,
          name: 'Стейк из тунца',
          count: 2,
          oldPrice: 500,
          newPrice: 250,
        },
      ],
      shopItems: [
        {
          id: 1,
          name: 'Продукт1',
          count: 2,
          img: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          oldPrice: 500,
          newPrice: 250,
        },
        {
          id: 2,
          name: 'Продукт2',
          count: 2,
          img: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          oldPrice: 500,
          newPrice: 250,
        },
        {
          id: 3,
          name: 'Продукт3',
          count: 2,
          img: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          oldPrice: 500,
          newPrice: 250,
        },
        {
          id: 4,
          name: 'Продукт4',
          count: 2,
          img: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          oldPrice: 500,
          newPrice: 250,
        },
        {
          id: 5,
          name: 'Продукт5',
          count: 2,
          img: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          oldPrice: 500,
          newPrice: 250,
        },
      ]
    };
  },
  methods: {
    _addItemInBasket(item) {
      const pushItem = {
        id: item.id,
        name: item.name,
        count: 1,
        oldPrice: item.oldPrice,
        newPrice: item.newPrice,
      }
      if ((!this.shopBasketItems.some(itemBasket => itemBasket.id === item.id))) {
        this.shopBasketItems.push(pushItem)
      }
    },

    _addCount(id) {
      console.log('add', id)
    },

    _clearShopBasket() {
      this.shopBasketItems = [];
    },
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
  top: 840px;
}
</style>