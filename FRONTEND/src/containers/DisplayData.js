import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import "./DisplayData.css";
import {Bar} from 'react-chartjs-2';
import {Line} from 'react-chartjs-2';
import Loader from 'react-loader-spinner';
import DateTimePicker from 'react-datetime-picker';
import GetData from './GetData';
export default class DisplayData extends Component {

    EndingDealers = {
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
              65, 59, 80, 81, 56, 55, 65, 59, 80, 81, 56, 55] // this.state.chartsData.EndingDealers
          }
        ]
      };
      
    RealisedDealers = {
          labels: ["Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia"],
          datasets: [
            {
              label: 'My First dataset',
              backgroundColor: 'rgba(255,99,132,0.2)',
              borderColor: 'rgba(255,99,132,1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255,99,132,0.4)',
              hoverBorderColor: 'rgba(255,99,132,1)',
              data: [65, 59, 80, 81, 56, 55] // this.state.chartsData.RealisedDealers
            }
          ]
      };
      
    effectiveDealers = {
          labels: ["Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia"],
          datasets: [
            {
              label: 'My First dataset',
              backgroundColor: 'rgba(255,99,132,0.2)',
              borderColor: 'rgba(255,99,132,1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255,99,132,0.4)',
              hoverBorderColor: 'rgba(255,99,132,1)',
              data: [65, 59, 80, 81, 56, 55]  // this.state.chartsData.effectiveDealers
            }
          ]
      };
      
    endingAggregated = {
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
          data: [65, 59, 80, 81, 56, 55, 40, 10, 20, 30, 40, 50]  // this.state.chartsData.endingAggregated
          }
      ]
      };
      
    realisedAggregated = 100500; // this.state.chartsData.realisedAggregated
      
    effectiveAggregated = 200400; // this.state.chartsData.effectiveAggregated
      
    averageData = {
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
              data: [59, 80, 81, 56, 55, 40, 10, 20, 30, 40, 50, 65] // this.state.chartsData.averageBuy
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
              data: [10, 20, 30, 40, 50, 65, 59, 80, 81, 56, 55, 40] // this.state.chartsData.averageSell
            }
          ]
      };

    constructor(props) {
        super(props);    
        this.state = {
          chartsData: ""
        };
    }

    getChartsUrl(id){
        switch(id){
            case "averageData": return "http://localhost:5001/average";
            case "endingDealers": return "http://localhost:5001/dealers_position";
            case "realisedDealers": return "http://localhost:5001/realised_profit_loss_dealers";
            case "effectiveDealers": return "http://localhost:5001/effective_profit_loss_dealers";
            case "endingAggregated": return "http://localhost:5001/aggregated_ending";
            case "realisedAggregated": return "http://localhost:5001/aggregated_effective";
            case "effectiveAggregated": return "http://localhost:5001/aggregated_realised";
        }
    }

    handleChartDataSubmit = async event => {
        var sel = document.getElementById("charts");
        var id = sel.options[sel.selectedIndex].value;
        console.log(id);
        document.getElementById('loader').style.display = 'block';
        var url = this.getChartsUrl(id);
        console.log(url);
        fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              start: document.getElementsByClassName("react-datetime-picker__inputGroup")[0].children[0].value,
              end: document.getElementsByClassName("react-datetime-picker__inputGroup")[1].children[0].value,
            }),
            mode: "cors"
        })
        .then(res => res)
        .then(
        (result) => {
            console.log(result);
            //todo change the vars
            this.setState ({
                chartsData: result
            }) 
            document.getElementById('loader').style.display = 'none';        
        },
        (error) => {
            console.log("ERROR in charts " + error);
            document.getElementById('loader').style.display = 'none'; 
        }
        );
    }

    renderSuccess() {
        return (
            <div>
            <GetData/>
            <div style={{alignItems:'center', textAlign:'center'}}>
            <select id="charts" onChange={this.handleChartDataSubmit} style={{width:'100%', marginTop:'10px'}}>
                <option disabled selected value> -- select an option -- </option>
                <option value="averageData">Average buy and sell prices for each instrument during the period</option>
                <option value="endingDealers">Ending positions for each dealer</option>
                <option value="realisedDealers">Realised profit/loss for each dealer</option>
                <option value="effectiveDealers">Effective profit/loss for each dealer</option>
                <option value="endingAggregated">Ending positions aggregated for all dealers</option>
                <option value="realisedAggregated">Realised profit/loss for aggregated for all dealers</option>
                <option value="effectiveAggregated">Effective profit/loss aggregated for all dealers</option>
            </select>
            <div style={{display: 'inline-flex', marginTop: '10px', enabled: false, pointerEvents:'none'}}>
                <p style={{marginLeft:'10px', marginRight:'10px'}}>Start</p>
                <DateTimePicker style={{marginLeft:'10px', marginRight:'10px', enabled: false}}
                    amPmAriaLabel="Select AM/PM"
                    calendarAriaLabel="Toggle calendar"
                    clearAriaLabel="Clear value"
                    dayAriaLabel="Day"
                    hourAriaLabel="Hour"
                    maxDetail="second"
                    minuteAriaLabel="Minute"
                    monthAriaLabel="Month"
                    nativeInputAriaLabel="Date and time"
                    secondAriaLabel="Second"
                    value={new Date() - 1000 * 120} // pass 2 min ago for 1 day data
                    yearAriaLabel="Year"/>
                <p style={{marginLeft:'10px', marginRight:'10px'}}>End</p>
                <DateTimePicker style={{marginLeft:'10px', marginRight:'10px', enabled: false}}
                    amPmAriaLabel="Select AM/PM"
                    calendarAriaLabel="Toggle calendar"
                    clearAriaLabel="Clear value"
                    dayAriaLabel="Day"
                    hourAriaLabel="Hour"
                    maxDetail="second"
                    minuteAriaLabel="Minute"
                    monthAriaLabel="Month"
                    nativeInputAriaLabel="Date and time"
                    secondAriaLabel="Second"
                    value={Date()}
                    yearAriaLabel="Year"/>
            </div>
            <div id="loader" style={{marginTop:'10px', display:'none'}} >
                <Loader type="Oval" color="#0018A8" height={80} width={80}/>
            </div>
            <div>
                <div id="averageData" style={{display:'none'}}>
                    <h4>Average buy and sell prices for each instrument during the period</h4>
                    <Line data={this.averageData} width={100}
                    height={50}/>           
                </div>
                <div id="endingDealers" style={{display:'none'}}>
                    <h4>Ending positions for each dealer</h4>
                    <Bar
                    data={this.EndingDealers}
                    height={150}
                    options={{
                        maintainAspectRatio: false
                    }}
                    />
                </div>
                <div id="realisedDealers" style={{display:'none'}}>
                    <h4>Realised profit/loss for each dealer</h4>
                    <Bar
                    data={this.RealisedDealers}
                    width={100}
                    height={50}
                    options={{
                        maintainAspectRatio: false
                    }}
                    />
                </div>
                <div id="effectiveDealers" style={{display:'none'}}>
                    <h4>Effective profit/loss for each dealer</h4> 
                    <Bar
                    data={this.effectiveDealers}
                    width={100}
                    height={50}
                    options={{
                        maintainAspectRatio: false
                    }}
                    />
                </div>
                <div id="endingAggregated" style={{display:'none'}}>
                    <h4>Ending positions aggregated for all dealers</h4>
                    <Bar
                    data={this.endingAggregated}
                    width={100}
                    height={50}
                    options={{
                        maintainAspectRatio: false
                    }}
                    />
                </div>
                <div id="realisedAggregated" style={{display:'none'}}>
                    <h4>Realised profit/loss for aggregated for all dealers</h4>
                    <p>{this.realisedAggregated}</p>
                </div>
                <div id="effectiveAggregated" style={{display:'none'}}>
                    <h4>Effective profit/loss aggregated for all dealers</h4>
                    <p>{this.effectiveAggregated}</p>
                </div>
            </div>
          </div>
          </div>       
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