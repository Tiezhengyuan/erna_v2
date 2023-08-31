<template>
  <div class="container">
    <div class="name">
      <label>{{data.label}}</label>
    </div>
    <ul class="value">
      <li v-for="(p,i) in data.options" :key="i">
        <input type="checkbox"
          :name="data.name"
          :value="p.value"
          :checked="p.checked"
          @change="add"
        />{{p.label}}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    name:'inputCheckbox',
    props:['data', 'receive'],
    methods:{
      add(e){
        for(let p of this.data.options){
            if (p.value==e.target.value){
              p.checked = e.target.checked
              break
            }
        }
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
  .container .value{
    margin: 0;
    padding: 0;
  }
  .container .value li{
    list-style-type: none;
  }

</style>