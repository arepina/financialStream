import React from "react";
import { Route, Switch } from "react-router-dom";
import NotFound from "./containers/NotFound";
import Login from "./containers/Login"
import DisplayData from "./containers/DisplayData"

export default () =>
  <Switch>
    <Route path="/" exact component={Login} />
    <Route path="/displaydata" exact component={DisplayData}/>
    <Route component={NotFound} />
  </Switch>;
