import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import Button from './Button.js'


export default class App extends Component {
  constructor(){
      super();

      this.state= {
          count: 0
      };
  }

  increment = () => {
      this.setState({
          count: this.state.count + 1
      });
  }

  decrement = () => {
      this.setState({
          count: this.state.count - 1
      });
  }

  render() {
    let { count } = this.state
    return (
      <div>
        <h2>Count: { count } </h2>
        <Button
          name = { "+" }
          todo = { () => this.increment() }
        />
        <Button
          name = { "-" }
          todo = { () => this.decrement() }
        />
       </div>
    );
  }

}
