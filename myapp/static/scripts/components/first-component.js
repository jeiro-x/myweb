import { LitElement, css, html } from '/static/scripts/lit.js';


class MiComponente extends LitElement {
  render() {
    return html`
      <p>Flare Hensonn000!</p>
    `;
  }
}

customElements.define('mi-componente', MiComponente);

// CONTENEDOR DEL FORMULARIOS
class FormContent extends LitElement {
  static styles = css`
    :host {
      display: block;
      margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background: #f9f9f9;
    }
  `;
    // createRenderRoot() {
    //     return this;
    // }

  render() {
    return html`
      <div>
      <slot></slot>
      </div>
    `;
  }
}

customElements.define('form-content', FormContent);

// COMPONENTE INPUT
class MyInput extends LitElement {
    static get properties(){
        return{
            label: {type: String},
            value: {type: String},
            name: {type: String}
        };
    }
    
    static get styles() {
        return css`
          :host {
            display: flex;
            flex-direction:column;
          }

          input {
            padding: 10px;
            border: 1px solid gray;
            border-radius: 5px;
            font-size: 16px;
            width: 50%;
            margin: 0px 0px 10px 0px
          }
          label{
            margin: 5px 0px;
          }
        `;
      }
      createRenderRoot() {
        return this;
    }
    constructor(){
        super();
        this.label = '';
        this.value = '';
        this.name = '';
    }

  render() {
    return html`
        <label>${this.label}</label>

        <input type="text" value="${this.value}" .name=${this.name}
        @input=${this.handleInput}
        >
    `;
  }
  handleInput(event) {
    this.value = event.target.value;
  }
};

customElements.define('input-view', MyInput);

console.log("Papada");
