import React, { Component } from "react";
import { Button } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import "./DisplayData.css";
import DataTable from "./DataTable";

export default class DisplayData extends Component {
    constructor(props) {
        super(props);
    }

    renderSuccess() {
        return (
            <div>
                <p>Connection Successful!</p>
                <DataTable />
            </div>
        )
    }

    renderFail() {
        return (
            <div>
                <p>Connection Fail!</p>
                <NavLink to={{ pathname: "/" }} > Retry </NavLink>
            </div>
        )
    }

    render() {
        try {
            if (this.props.location && this.props.location.state.status) {
                console.log(this.props.location.state);
                return this.renderSuccess()
            }
            else {
                console.log(this.props.location);
                return this.renderFail()
            }
        }
        catch (TypeError) {
            this.props.history.push('/');
            return ("Please login again");
        }
    }
}