import React from "react";
import { Route, Switch } from "react-router-dom";
import NotFound from "./containers/NotFound";
import Login from "./containers/Login"
import DisplayData from "./containers/DisplayData"

export default (props) =>
  <Switch>
    <Route path="/" exact component={Login} />
    {/* <Route path="/login" exact component={Login} />
    <Route path="/signup" exact component={Signup}/> */}
    <Route path="/displaydata" exact component={DisplayData}/>
    <Route component={NotFound} />
    {/* {props.loggedInStatus ? } */}
  </Switch>;
