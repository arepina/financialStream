import React, { Component } from "react";
import { Button } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import "./DisplayData.css";
import {Bar} from 'react-chartjs-2';
import {Line} from 'react-chartjs-2';

const EndingDealers = {
  labels: ["Lewis Astronomica", "Lewis Borealis", "Lewis Celestial", "Lewis Deuteronic", "Lewis Eclipse",
"Lewis Floral", "Lewis Galactia", "Lewis Heliosphere", "Lewis Interstella", "Lewis Jupiter", "Lewis Koronis", "Lewis Lunatic",

"Selvyn Astronomica", "Selvyn Borealis", "Selvyn Celestial", "Selvyn Deuteronic", "Selvyn Eclipse",
"Selvyn Floral", "Selvyn Galactia", "Selvyn Heliosphere", "Selvyn Interstella", "Selvyn Jupiter", "Selvyn Koronis", "Selvyn Lunatic",

"Richard Astronomica", "Richard Borealis", "Richard Celestial", "Richard Deuteronic", "Richard Eclipse",
"Richard Floral", "Richard Galactia", "Richard Heliosphere", "Richard Interstella", "Richard Jupiter", "Richard Koronis", "Richard Lunatic",

"Lina Astronomica", "Lina Borealis", "Lina Celestial", "Lina Deuteronic", "Lina Eclipse",
"Lina Floral", "Lina Galactia", "Lina Heliosphere", "Lina Interstella", "Lina Jupiter", "Lina Koronis", "Lina Lunatic",

"John Astronomica", "John Borealis", "John Celestial", "John Deuteronic", "John Eclipse",
"John Floral", "John Galactia", "John Heliosphere", "John Interstella", "John Jupiter", "John Koronis", "John Lunatic",

"Nidia Astronomica", "Nidia Borealis", "Nidia Celestial", "Nidia Deuteronic", "Nidia Eclipse",
"Nidia Floral", "Nidia Galactia", "Nidia Heliosphere", "Nidia Interstella", "Nidia Jupiter", "Nidia Koronis", "Nidia Lunatic"],


  datasets: [
    {
      label: 'My First dataset',
      backgroundColor: 'rgba(255,99,132,0.2)',
      borderColor: 'rgba(255,99,132,1)',
      borderWidth: 1,
      hoverBackgroundColor: 'rgba(255,99,132,0.4)',
      hoverBorderColor: 'rgba(255,99,132,1)',
      data: [65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55,
        65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55,
        65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55,
        65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55,
        65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55,
        65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55]
    }
  ]
};

const RealisedDealers = {
    labels: ["Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia"],
    datasets: [
      {
        label: 'My First dataset',
        backgroundColor: 'rgba(255,99,132,0.2)',
        borderColor: 'rgba(255,99,132,1)',
        borderWidth: 1,
        hoverBackgroundColor: 'rgba(255,99,132,0.4)',
        hoverBorderColor: 'rgba(255,99,132,1)',
        data: [65, 59, 80, 81, 56, 55]
      }
    ]
  };

const effectiveDealers = {
    labels: ["Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia"],
    datasets: [
      {
        label: 'My First dataset',
        backgroundColor: 'rgba(255,99,132,0.2)',
        borderColor: 'rgba(255,99,132,1)',
        borderWidth: 1,
        hoverBackgroundColor: 'rgba(255,99,132,0.4)',
        hoverBorderColor: 'rgba(255,99,132,1)',
        data: [65, 59, 80, 81, 56, 55]
      }
    ]
  };

  const endingAggregated = {
    labels: ["Astronomica", "Borealis", "Celestial", "Deuteronic", "Eclipse",
    "Floral", "Galactia", "Heliosphere", "Interstella", "Jupiter", "Koronis", "Lunatic"],
    datasets: [
      {
        label: 'My First dataset',
        backgroundColor: 'rgba(255,99,132,0.2)',
        borderColor: 'rgba(255,99,132,1)',
        borderWidth: 1,
        hoverBackgroundColor: 'rgba(255,99,132,0.4)',
        hoverBorderColor: 'rgba(255,99,132,1)',
        data: [65, 59, 80, 81, 56, 55, 40, 10, 20, 30, 40, 50]
      }
    ]
  };

const realisedAggregated = 100500;

const effectiveAggregated = 200400;

const averageData = {
    labels: ["Astronomica", "Borealis", "Celestial", "Deuteronic", "Eclipse",
    "Floral", "Galactia", "Heliosphere", "Interstella", "Jupiter", "Koronis", "Lunatic"],
    datasets: [
      {
        label: 'Buy price',
        fill: false,
        lineTension: 0.1,
        backgroundColor: 'rgba(255,192,192,0.4)',
        borderColor: 'rgba(255,192,192,1)',
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBorderColor: 'rgba(255,192,192,1)',
        pointBackgroundColor: '#fff',
        pointBorderWidth: 1,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: 'rgba(255,192,192,1)',
        pointHoverBorderColor: 'rgba(220,220,220,1)',
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [65, 59, 80, 81, 56, 55, 40, 10, 20, 30, 40, 50]
      },
      {
        label: 'Sell price',
        fill: false,
        lineTension: 0.1,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBorderColor: 'rgba(75,192,192,1)',
        pointBackgroundColor: '#fff',
        pointBorderWidth: 1,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: 'rgba(75,192,192,1)',
        pointHoverBorderColor: 'rgba(220,220,220,1)',
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [10, 20, 30, 40, 50, 65, 59, 80, 81, 56, 55, 40]
      }
    ]
  };


export default class DisplayData extends Component {
    constructor(props) {
        super(props);
    }

    renderSuccess() {
        return (
            <div>
            <div>
                <h4>Average buy and sell prices for each instrument during the period</h4>
                <Line data={averageData} width={100}
                height={50}/>           
            </div>
            <div>
                <h4>Ending positions for each dealer</h4>
                <Bar
                data={EndingDealers}
                height={150}
                options={{
                    maintainAspectRatio: false
                }}
                />
            </div>
            <div>
                <h4>Realised profit/loss for each dealer </h4>
                <Bar
                data={RealisedDealers}
                width={100}
                height={50}
                options={{
                    maintainAspectRatio: false
                }}
                />
            </div>
            <div>
                <h4>Effective profit/loss for each dealer</h4> 
                <Bar
                data={effectiveDealers}
                width={100}
                height={50}
                options={{
                    maintainAspectRatio: false
                }}
                />
            </div>
            <div>
                <h4>Ending positions aggregated for all dealers</h4>
                <Bar
                data={endingAggregated}
                width={100}
                height={50}
                options={{
                    maintainAspectRatio: false
                }}
                />
            </div>
            <div>
                <h4>Realised profit/loss for aggregated for all dealers</h4>
                <p>{realisedAggregated}</p>
            </div>
            <div>
                <h4>Effective profit/loss aggregated for all dealers</h4>
                <p>{effectiveAggregated}</p>
            </div>
          </div>       
        )
    }

    renderFail() {
        return (
            <div>
                <p>Connection Fail!</p>
                <NavLink to={{pathname: "/login"}} > Retry </NavLink>
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