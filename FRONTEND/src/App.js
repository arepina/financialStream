import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Nav, Navbar, NavItem } from "react-bootstrap";
import "./App.css";
import Routes from "./Routes";
import { LinkContainer } from "react-router-bootstrap";

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      loggedInStatus: false
    }
  }

  // state: loggedInStatus - boolean
  render() {
    return (
      <div className="App container">
        <Navbar fluid collapseOnSelect>
          <Navbar.Header>
            <Navbar.Brand>
              <Link to="/">Scratch</Link>
            </Navbar.Brand>
            <Navbar.Toggle />
          </Navbar.Header>
          <Navbar.Collapse>
          <Nav pullRight>
          <LinkContainer to="/signup">
              <NavItem>Signup</NavItem>
            </LinkContainer>
            {/* if loggedInStatus is false - ternary else display logout*/}
            <LinkContainer to="/login">
              <NavItem>Login</NavItem>
            </LinkContainer>
            
          </Nav>
        </Navbar.Collapse>
        </Navbar>
        <Routes loggedInStatus={loggedInStatus}/>
      </div>
    );
  }
}

export default App;
