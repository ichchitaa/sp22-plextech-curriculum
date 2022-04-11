import React, { Component } from 'react'
export default class Button extends Component {
    render() {
        let { name, todo } = this.props;
        return (
            <button onClick = { todo }>{ name }</button>
        );
    }
}