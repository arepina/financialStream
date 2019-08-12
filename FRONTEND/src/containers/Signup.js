import React, { Component } from "react";
import {
  HelpBlock,
  FormGroup,
  FormControl,
  ControlLabel,
  ButtonGroup,
  Button
} from "react-bootstrap";
import LoaderButton from "../components/LoaderButton";
import "./Signup.css";

export default class Signup extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      username: "",
      password: "",
      confirmPassword: ""
    };

    this.onRadioBtnClick = this.onRadioBtnClick.bind(this);
  }

  validateForm() {
    return (
      this.state.username.length > 0 &&
      this.state.password.length > 0 &&
      this.state.password === this.state.confirmPassword
    );
  }

  onRadioBtnClick(rSelected) {
    this.setState({ rSelected });
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = async event => {
    event.preventDefault();

    let url = '';

    fetch(url, {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        login: this.state.username,
        password: this.state.password,
        userType: this.state.rSelected
      }),
      credentials: 'same-origin'
    })
      .then(res => res.json())
      .then(function (res) {
        console.log(res)
      })
      .catch(function (error) {
        alert(error)
      });

    this.setState({ isLoading: true });
  }

  renderForm() {
    return (
      <form onSubmit={this.handleSubmit}>
        <FormGroup controlId="username" bsSize="large">
          <ControlLabel>Username</ControlLabel>
          <FormControl
            autoFocus
            type="username"
            value={this.state.username}
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
        <FormGroup controlId="confirmPassword" bsSize="large">
          <ControlLabel>Confirm Password</ControlLabel>
          <FormControl
            value={this.state.confirmPassword}
            onChange={this.handleChange}
            type="password"
          />
        </FormGroup>
        <FormGroup controlId="usertype" bsSize="large">
          <ControlLabel>User Type: </ControlLabel>
          <ButtonGroup>
            <Button color="primary" onClick={() => this.onRadioBtnClick("Security Officer")} active={this.state.rSelected === "Security Officer"}>Security Officer</Button>
            <Button color="primary" onClick={() => this.onRadioBtnClick("Trader")} active={this.state.rSelected === "Trader"}>Trader</Button>
            <Button color="primary" onClick={() => this.onRadioBtnClick("System Architect")} active={this.state.rSelected === "System Architect"}>System Architect</Button>
            <Button color="primary" onClick={() => this.onRadioBtnClick("Senior Trader")} active={this.state.rSelected === "Senior Trader"}>Senior Trader </Button>
          </ButtonGroup>
        </FormGroup>
        <LoaderButton
          block
          bsSize="large"
          disabled={!this.validateForm()}
          type="submit"
          isLoading={this.state.isLoading}
          text="Signup"
          loadingText="Signing up…"
        />
      </form>
    );
  }

  render() {
    return (
      <div className="Signup">
        {this.renderForm()}
      </div>
    );
  }
}
