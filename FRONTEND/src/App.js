import React, { Component } from "react";
import { Navbar} from "react-bootstrap";
import "./App.css";
import Routes from "./Routes";

class App extends Component {

  render() {
    return (
      <div className="App container">
        <Navbar fluid collapseOnSelect style={{background:'#0018A8'}}>
          <Navbar.Header>
            <Navbar.Brand style={{color: 'white'}}>
            DB.Deals
              {/* <Link to="/" style={{color: 'white'}}>DB.Deals</Link> */}
            </Navbar.Brand>
            <img src={require('./deutschebank.png')} width='32px' height='32px' style={{marginTop:'7px'}}/>
          </Navbar.Header>
        </Navbar>
        <Routes />
      </div>
    );
  }
}

export default App;
