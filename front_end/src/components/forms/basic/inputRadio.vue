<template>
  <div class="container">
    <div class="name">
      <label>{{data.label}}</label>
    </div>
    <div class="value" v-for="(p,i) of data.options" :key="i">
      <input type="radio"
        :name="data.name"
        :value="p"
        @change="add"
      />{{p}}
    </div>
  </div>
</template>

<script>
export default {
    name:'inputRadio',
    props:['data', 'receive'],
    methods:{
      add(e){
        this.data.value = e.target.value
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