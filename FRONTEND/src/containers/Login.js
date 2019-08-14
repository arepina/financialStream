import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
// import { Link } from "react-router-bootstrap";
import { NavLink } from "react-router-dom";
import "./Login.css";
import  DisplayData from "./DisplayData";

export default class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
      loggedInStatus: false,
      connectStatus: false
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

    fetch('https://jsonplaceholder.typicode.com/posts', {
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
          console.log(result);
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
          console.error("Login error!")
          alert("Login failed. Please try again.")
          this.setState({
            loggedInStatus: false
          })
        }
      )
  }

  handleDisplayDataSubmit = async event => {
    event.preventDefault();

    fetch('https://jsonplaceholder.typicode.co/posts', {
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
          console.log(result);
          if (parseInt(result.status / 100) === 2) {
            this.setState ({
              connectStatus: true
            })
            console.log("connect status: " + this.state.connectStatus)
            this.props.history.push('/displaydata', { status: true});
          }
          else {
            this.setState ({
              connectStatus: false
            })
            this.props.history.push('/displaydata', { status: false});
          }
        },
        (error) => {
          this.setState ({
            connectStatus: false
          })
          this.props.history.push('/displaydata', {status: false});
        }
      )
  }

  renderSuccess() {
    return (
        <p>Connection Successful!</p>
    )
}

renderFail() {
    return (
        <div>
            <p>Connection Fail!</p>
            <NavLink to={{pathname: "/"}} > Retry </NavLink>
        </div>
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
          <Button
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

  renderDisplayData() {
    return (
      <div>
        <p> Successsfully connected!</p>
        <p> Data here!</p>
      </div>
    )
  }



  render() {
    if (this.state.loggedInStatus) {
      return (
        <div>
          <p> Login Successsfully!</p>
            <Button onClick={this.handleDisplayDataSubmit}> Continue </Button>
        </div>
      )
    }
    else {
      return (this.renderLogin())
    }
  }
}
