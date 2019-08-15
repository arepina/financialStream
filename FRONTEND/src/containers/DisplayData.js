import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import "./DisplayData.css";
import {Bar} from 'react-chartjs-2';
import {Line} from 'react-chartjs-2';
import Loader from 'react-loader-spinner';
import DateTimePicker from 'react-datetime-picker';
import TableData from './TableData';
import baseUrl from "./Utils";
export default class DisplayData extends Component {

    constructor(props) {
        super(props);
        this.state = {
          averageSellData: [0,0,0,0,0,0,0,0,0,0,0,0],
          averageBuyData: [0,0,0,0,0,0,0,0,0,0,0,0],
          effectiveAggregatedData: 0,
          realisedAggregatedData: 0,
          endingAggregatedData: [0,0,0,0,0,0,0,0,0,0,0,0],
          effectiveDealersData: [0,0,0,0,0,0],
          realisedDealersData:  [0,0,0,0,0,0],
          endingDealersData: [0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0],
        };
        this.setState({
          endingDealers : {
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
                   data: this.state.endingDealersData
                 }
               ]
             },
          realisedDealers : {
                 labels: ["Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia"],
                 datasets: [
                   {
                     label: 'My First dataset',
                     backgroundColor: 'rgba(255,99,132,0.2)',
                     borderColor: 'rgba(255,99,132,1)',
                     borderWidth: 1,
                     hoverBackgroundColor: 'rgba(255,99,132,0.4)',
                     hoverBorderColor: 'rgba(255,99,132,1)',
                     data: this.state.realisedDealersData
                   }
                 ]
             },
          effectiveDealers : {
                 labels: ["Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia"],
                 datasets: [
                   {
                     label: 'My First dataset',
                     backgroundColor: 'rgba(255,99,132,0.2)',
                     borderColor: 'rgba(255,99,132,1)',
                     borderWidth: 1,
                     hoverBackgroundColor: 'rgba(255,99,132,0.4)',
                     hoverBorderColor: 'rgba(255,99,132,1)',
                     data: this.state.effectiveDealersData
                   }
                 ]
             },
          endingAggregated : {
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
                 data: this.state.endingAggregatedData
                 }
             ]
           },
          realisedAggregated : this.state.realisedAggregatedData,
          effectiveAggregated : this.state.effectiveAggregatedData,
          averageData : {
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
                     data: this.state.averageBuyData
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
                     data: this.state.averageSellData
                   }
                 ]
             }
           });
    }

    getChartsUrl(id){
        switch(id){
            case "averageData": return baseUrl + '/average';
            case "endingDealers": return baseUrl + '/dealers_position';
            case "realisedDealers": return baseUrl + '/realised_profit_loss_dealers';
            case "effectiveDealers": return baseUrl + '/effective_profit_loss_dealers';
            case "endingAggregated": return baseUrl + '/aggregated_ending';
            case "realisedAggregated": return baseUrl + '/aggregated_effective';
            case "effectiveAggregated": return baseUrl + '/aggregated_realised';
        }
    }

    hideAll(){
        document.getElementById('averageData').style.display = 'none';
        document.getElementById('endingDealers').style.display = 'none';
        document.getElementById('realisedDealers').style.display = 'none';
        document.getElementById('effectiveDealers').style.display = 'none';
        document.getElementById('endingAggregated').style.display = 'none';
        document.getElementById('realisedAggregated').style.display = 'none';
        document.getElementById('effectiveAggregated').style.display = 'none';
    }

    handleChartDataSubmit = async event => {
        this.hideAll();
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
        .then((response) => response.json())
        .then((result) => {
            console.log(url);
            console.log(result);
            switch(url){
              case  'http://localhost:5001/average' : {
                this.state.averageBuyData = result.averageBuy;
                this.state.averageSellData = result.averageSell;
                console.log(this.state.averageBuyData);
                console.log(result.averageBuy);
                document.getElementById('averageData').style.display = 'block';
                break;
              }
              case  'http://localhost:5001/dealers_position' : {
                this.state.effectiveAggregatedData = result.effectiveAggregated;
                document.getElementById('effectiveAggregated').style.display = 'block';
                break;
              }
              case  'http://localhost:5001/realised_profit_loss_dealers' : {
                this.state.realisedAggregatedData = result.realisedAggregated;
                document.getElementById('realisedAggregated').style.display = 'block';
                break;
              }
              case  'http://localhost:5001/effective_profit_loss_dealers:' : {
                this.state.endingAggregatedData = result.endingAggregated;
                document.getElementById('endingAggregated').style.display = 'block';
                break;
              }
              case  'http://localhost:5001/aggregated_ending' : {
                this.state.effectiveDealersData = result.effectiveDealers;
                document.getElementById('effectiveDealers').style.display = 'block';
                break;
              }
              case  'http://localhost:5001/aggregated_effective' : {
                this.state.realisedDealersData = result.realisedDealers;
                document.getElementById('realisedDealers').style.display = 'block';
                break;
              }
              case  'http://localhost:5001/aggregated_realised' : {
                this.state.endingDealersData = result.endingDealers;
                document.getElementById('endingDealers').style.display = 'block';
                break;
              }
            }
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
            <TableData/>
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
                    value={new Date() - 1000 * 3600 * 24 * 365} // 1 year before today
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
                    <Line data={this.state.averageData} width={100}
                    height={50}/>
                </div>
                <div id="endingDealers" style={{display:'none'}}>
                    <h4>Ending positions for each dealer</h4>
                    <Bar
                    data={this.state.endingDealers}
                    height={150}
                    options={{
                        maintainAspectRatio: false
                    }}
                    />
                </div>
                <div id="realisedDealers" style={{display:'none'}}>
                    <h4>Realised profit/loss for each dealer</h4>
                    <Bar
                    data={this.state.realisedDealers}
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
                    data={this.state.effectiveDealers}
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
                    data={this.state.endingAggregated}
                    width={100}
                    height={50}
                    options={{
                        maintainAspectRatio: false
                    }}
                    />
                </div>
                <div id="realisedAggregated" style={{display:'none'}}>
                    <h4>Realised profit/loss for aggregated for all dealers</h4>
                    <p>{this.state.realisedAggregated}</p>
                </div>
                <div id="effectiveAggregated" style={{display:'none'}}>
                    <h4>Effective profit/loss aggregated for all dealers</h4>
                    <p>{this.state.effectiveAggregated}</p>
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
