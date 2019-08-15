import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import "./Login.css";
import baseUrl from "./Utils";

export default class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
      loggedInStatus: false
    };
  }

  validateForm() {
    return this.state.username.length > 0 && this.state.password.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleLoginSubmit = async event => {
    event.preventDefault();
    const url = baseUrl + '/login'
    fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        login: this.state.email,
        password: this.state.password,
      }),
      //credentials: 'same-origin'
      mode: "cors"
    })
      .then(res => res)
      .then(
        (result) => {
          if (parseInt(result.status / 100) === 2) {
            this.setState({
              loggedInStatus: true
            })
          }
          else {
            alert("Login failed. Please try again.")
            this.setState({
              loggedInStatus: false
            })
          }
        },
        (error) => {
          alert("Login failed. Please try again.")
          this.setState({
            loggedInStatus: false
          })
        }
      )
  }

  handleDisplayDataSubmit = async event => {
    event.preventDefault();
    const url = baseUrl + '/connection'
    fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      //credentials: 'same-origin'
      mode: "cors"
    })
      .then(res => res)
      .then(
        (result) => {
          if (parseInt(result.status / 100) === 2) {
            this.props.history.push('/displaydata', { status: true, username: this.state.username});
          }
          else {
            this.props.history.push('/displaydata', { status: false});
          }
        },
        (error) => {
          this.props.history.push('/displaydata', {status: false});
        }
      )
  }

  renderLogin() {
    return (
      <div className="Login">
        <form onSubmit={this.handleLoginSubmit}>
          <FormGroup controlId="username" bsSize="large">
            <ControlLabel>Username</ControlLabel>
            <FormControl
              autoFocus
              value={this.state.Username}
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="password" bsSize="large">
            <ControlLabel>Password</ControlLabel>
            <FormControl
              value={this.state.password}
              onChange={this.handleChange}
              type="password"
            />
          </FormGroup>
          <Button style={{background:'#0018A8', color: 'white'}}
            block
            bsSize="large"
            disabled={!this.validateForm()}
            type="submit"
          >
            Login
          </Button>
        </form>
      </div>
    )
  }

  render() {
    const divStyle = {
      justifycontent: 'center', 
      display: 'grid'
    };
    if (this.state.loggedInStatus) {
      return (
        <div style={divStyle}>
          <h3 style={{textAlign:'center', fontWeight: 'bold'}}> Welcome, {this.state.username}!</h3>
          <div style={{textAlign:'center'}}>
            <Button  style={{
              background:'#0018A8', color: 'white', width: '100px', 
              fontWeight: 'bold', padding: '10px'
              }} onClick={this.handleDisplayDataSubmit}> Continue 
            </Button>
          </div>
        </div>
      )
    }
    else {
      return (this.renderLogin())
    }
  }
}
