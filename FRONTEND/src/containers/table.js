import React from 'react';
import { Table } from 'reactstrap';
import React, { Component } from 'react'


class Table extends Component {
    constructor(props) {
       super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
       this.state = { //state is by default an object
           data: [//
        //      { id: 1, name: 'Wasif', age: 21, email: 'wasif@email.com' },
        //      { id: 2, name: 'Ali', age: 19, email: 'ali@email.com' },
        //      { id: 3, name: 'Saad', age: 16, email: 'saad@email.com' },
        //      { id: 4, name: 'Asad', age: 25, email: 'asad@email.com' }
        ]
       }
    }

    renderTableHeader() {
        let header = Object.keys(["id","instrumentName", "cpty", "price", "type", "quantity", "time"])
        return header.map((key, index) => {
           return <th key={index}>{key.toUpperCase()}</th>
        })
     }

    renderTableData() {
        return this.state.data.map((data, index) => {
           const { id, instrumentName, cpty, price, type, quantity, time } = data //destructuring
           return (
              <tr key={id}>
                 <td>{id}</td>
                 <td>{instrumentName}</td>
                 <td>{cpty}</td>
                 <td>{price}</td>
                 <td>{type}</td>
                 <td>{quantity}</td>
                 <td>{time}</td>
              </tr>
           )
        })
     }


  render() {
    return (
      <Table responsive>
        <thead>
          <tr>
            <th>#</th>
            <th>instrumentName</th>
            <th>cpty</th>
            <th>price</th>
            <th>type</th>
            <th>quantity</th>
            <th>time</th>
          </tr>
        </thead>
        <tbody>
          {this.renderTableData()}
        </tbody>
      </Table>
    );
  }
}