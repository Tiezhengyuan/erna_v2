<template>
  <div class="container">
    <div class="name">
      <label>{{data.label}}</label>
    </div>
    <div class="value">
      <input type="Range"
        :name="data.name"
        :value="data.value"
        :min="data.min"
        :max="data.max"
        @change="add"
      />{{data.value}}
    </div>
  </div>
</template>

<script>
export default {
    name:'inputRange',
    props:['data', 'receive'],
    methods:{
      add(e){
        this.data.value = Number(e.target.value)
        const obj = {
          [this.data.name]: this.data
        }
        this.receive(obj);
      }
    }
}
</script>

<style scoped>
  .container{
    padding: 5px;
    box-sizing: border-box;
    display:flex;
    flex-direction: row;
  }
  .container .name{
    width: 40%;
    padding-right: 10px;
    display:flex;
    justify-content: right;
  }


</style>