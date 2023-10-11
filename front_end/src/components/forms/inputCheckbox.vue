<template>
  <div class="container input-checkbox">
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
        />{{p.label}}</li>
    </ul>
  </div>
</template>

<script>
export default {
    name: 'inputCheckbox',
    props: ['data', 'receive'],
    methods: {
      add(e) {
        for (let p of this.data.options) {
            if (p.value==e.target.value) {
              p.checked = e.target.checked;
              break;
            }
        }
        this.receive(this.data);
      },
    },
};
</script>

<style scoped>
  .container.input-checkbox {
    padding: 5px;
    display: flex;
  }
  .container.input-checkbox .name {
    padding-right: 10px;
    font-weight: bold;
  }
  .container.input-checkbox .value {
    margin: 0;
    padding: 0;
  }
  .container.input-checkbox li {
    display: inline;
  }

</style>