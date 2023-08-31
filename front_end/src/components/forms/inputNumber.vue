<template>
  <div class="container">
    <div class="name">
      <label>{{data.label}}</label>
    </div>
    <div class="value">
      <input type="number" min="0"
        :name="data.name"
        :value="data.value"
        @keyup="add"
      />
    </div>
  </div>
</template>

<script>
export default {
    name:'inputNumber',
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