import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

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
          title = { "+" }
          task = { () => this.increment() }
        />
        <Button
          title = { "-" }
          task = { () => this.decrement() }
        />
       </div>
    );
  }

}
