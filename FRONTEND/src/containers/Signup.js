import React, { Component } from "react";
import {
  HelpBlock,
  FormGroup,
  FormControl,
  ControlLabel,
  Dropdown,
  DropdownButton,
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
      email: "",
      password: "",
      confirmPassword: "",
      confirmationCode: "",
      newUser: null
    };

    this.onRadioBtnClick = this.onRadioBtnClick.bind(this);
    //this.onCheckboxBtnClick = this.onCheckboxBtnClick.bind(this);
  }

  validateForm() {
    return (
      this.state.email.length > 0 &&
      this.state.password.length > 0 &&
      this.state.password === this.state.confirmPassword
    );
  }

  onRadioBtnClick(rSelected) {
    this.setState({ rSelected });
  }


  validateConfirmationForm() {
    return this.state.confirmationCode.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = async event => {
    event.preventDefault();

    let url = 'TO DO'  ;// put flask link here as a string!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TO DO!!!!!!!!!!!!!!!!!!!!!

    let data =  new FormData();
    data.append("email", this.state.email);
    data.append("password", this.state.password);
    data.append("user type", this.state.rSelected);
    fetch(url, {method: "POST", body: data, mode: "cors"}) 
       //.then(checkStatus)
       .then(res => res.json())
        .then(function(res) {
            console.log(res)
        })
       .catch(function(error) {
           alert(error)
       });




    this.setState({ isLoading: true });

    this.setState({ newUser: "test" });

    this.setState({ isLoading: false });
  }

  handleConfirmationSubmit = async event => {
    event.preventDefault();

    this.setState({ isLoading: true });
  }

  renderConfirmationForm() {
    return (
      <form onSubmit={this.handleConfirmationSubmit}>
        <FormGroup controlId="confirmationCode" bsSize="large">
          <ControlLabel>Confirmation Code</ControlLabel>
          <FormControl
            autoFocus
            type="tel"
            value={this.state.confirmationCode}
            onChange={this.handleChange}
          />
          <HelpBlock>Please check your email for the code.</HelpBlock>
        </FormGroup>
        <LoaderButton
          block
          bsSize="large"
          disabled={!this.validateConfirmationForm()}
          type="submit"
          isLoading={this.state.isLoading}
          text="Verify"
          loadingText="Verifying…"
        />
      </form>
    );
  }

  renderForm() {
    return (
      <form onSubmit={this.handleSubmit}>
        <FormGroup controlId="email" bsSize="large">
          <ControlLabel>Email</ControlLabel>
          <FormControl
            autoFocus
            type="email"
            value={this.state.email}
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



        <FormGroup controlId="usertype" bsSize="large">
        <ControlLabel>User Type: </ControlLabel>
        <ButtonGroup> 
          <Button color="primary" onClick={() => this.onRadioBtnClick("Security Officer")} active={this.state.rSelected === "Security Officer"}>Security Officer</Button>
          <Button color="primary" onClick={() => this.onRadioBtnClick("Trader")} active={this.state.rSelected === "Trader"}>Trader</Button>
          <Button color="primary" onClick={() => this.onRadioBtnClick("System Architect")} active={this.state.rSelected === "System Architect"}>System Architect</Button>
          <Button color="primary" onClick={() => this.onRadioBtnClick("Senior trader")} active={this.state.rSelected === "Senior trader"}>Senior trader </Button>

        </ButtonGroup>
        </FormGroup>



        <FormGroup controlId="confirmPassword" bsSize="large">
          <ControlLabel>Confirm Password</ControlLabel>
          <FormControl
            value={this.state.confirmPassword}
            onChange={this.handleChange}
            type="password"
          />
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
        {this.state.newUser === null
          ? this.renderForm()
          : this.renderConfirmationForm()}
      </div>
    );
  }
}
