import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./containers/Home";
import NotFound from "./containers/NotFound";
import Login from "./containers/Login"
import Signup from "./containers/Signup";
import DisplayData from "./containers/DisplayData"
import TableSample from "./containers/TableSample"

export default () =>
  <Switch>
    <Route path="/" exact component={Login} />
    {/* <Route path="/login" exact component={Login} />
    <Route path="/signup" exact component={Signup}/> */}
    <Route path="/displaydata" exact component={DisplayData}/>
    <Route path="/tablesample" component={TableSample}/>
    <Route component={NotFound} />
    {/* {props.loggedInStatus ? } */}
  </Switch>;
