<template>
  <div class="header">
    <el-row
            :gutter="692"
            class="el-row-wrapper"
    >
      <div class="header-wrapper">
        <el-col :span="40">
          <div
                  class="header-title-wrapper"
                  @click="_goHome"
          >
            <div class="header-title">
              <i class="el-icon-food"></i>
              #СПАСИ ЕДУ
            </div>
          </div>
        </el-col>
        <el-col :span="40">
          <div
                  class="menu-burger"
                  @click="openDrawer"
          >
            <i class="el-icon-s-fold" />
          </div>
        </el-col>
      </div>
    </el-row>
    <div>
      <drawer-menu ref="drawer"/>
    </div>
  </div>
</template>

<script>
  import DrawerMenu from './drawerMenu'

export default {
  name: 'HelloWorld',
  components: {
    DrawerMenu,
  },
  methods: {
    openDrawer() {
      this.$refs.drawer.open();
    },

    _goHome() {
      this.$router.push('/')
    }
  }
}
</script>

<style lang="scss" scoped>
  .el-row-wrapper {
    box-shadow: 0px -5px 15px 2px;
  }

  .header-wrapper {
    color: tomato;
    display: flex;
    justify-content: space-between;
    height: 60px;
    align-items: center;
    width: 98%;
    font-weight: bold;
    margin: 0 auto;
  }

  .header-title-wrapper {
    cursor: pointer;
    width: 130px;
    height: 50px;
  }

  .header-title {
    padding: 17px 0 15px;
  }

  .el-row-wrapper {
    background-color: azure;
    border-bottom: 1px solid #e2e2e2
  }

  .menu-burger {
    width: 34px;
    height: 34px;
    cursor: pointer;
  }

  .el-icon-s-fold {
    margin: 8px 8px;
  }
</style>