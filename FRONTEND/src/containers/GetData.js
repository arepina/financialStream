import React, { useState } from 'react';
import { useObservable } from 'rxjs-hooks';
import { Observable } from 'rxjs';
import { map, withLatestFrom, filter } from 'rxjs/operators';
import { Table, Input, Button } from 'reactstrap';
// import { ReactTable } from 'react-table';
import "./GetData.css";

const url = "http://localhost:8080/streamTime/sse";
const source = new EventSource(url);
const stringObservable = Observable.create(observer => {
    source.addEventListener('message', (messageEvent) => {
        // console.log(messageEvent);
        observer.next(messageEvent.data);
    }, false);
});

function GetData() {
    let streamingStatus = true;
    const myTable = "myTable";

    const [stringArray, setStringArray] = useState([]);

    useObservable(
        state =>
            stringObservable.pipe(
                withLatestFrom(state),
                map(([state]) => {
                    let updatedStringArray = stringArray;
                    updatedStringArray.unshift(state);
                    if (updatedStringArray.length >= 50) {
                        updatedStringArray.pop();
                    }
                    setStringArray(updatedStringArray);
                    return state;
                })
            )
    );

    const columns = [{
        Header: 'Id',
        accessor: 'id' // String-based value accessors!
    }, {
        Header: 'Clock',
        accessor: 'clock'
    }]

    const stopStreaming = event => {
        streamingStatus = false;
        console.log('Connection closed');
        source.close();
    }

    const filterFn = event => {
        // Declare variables 
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("myFilter");
        filter = input.value.toUpperCase();
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");
      
        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td")[0];
          console.log(td);
          if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
            } else {
              tr[i].style.display = "none";
            }
          } 
        }
    }

    return (
        <>
        <Input type="text" id="myFilter" onKeyPress={filterFn} placeholder="Filter for Instrument here..."></Input>
            <Table responsive id={myTable}>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>name</th>
                        <th>password</th>
                        {/* <th>instrumentName</th>
                        <th>cpty</th>
                        <th>price</th>
                        <th>type</th>
                        <th>quantity</th>
                        <th>time</th> */}
                    </tr>
                </thead>
                <tbody>
                    {
                        stringArray.map((message, index) => {
                            message = message.replace(/'/g, '"')
                            console.log("after " + message)
                            message = JSON.parse(message)
                            console.log(message)
                            // console.log(message.id)
                            // console.log(jsonMessgage.id + ' ' + jsonMessgage.name + ' ' + jsonMessgage.password)
                            return (
                                <tr key={index}>
                                    <td>{index}</td>
                                    <td>{message.name}</td>
                                    <td>{message.password}</td>
                                    {/* <td>{instrumentName}</td>
                                <td>{cpty}</td>
                                <td>{price}</td>
                                <td>{type}</td>
                                <td>{quantity}</td>
                                <td>{time}</td> */}
                                </tr>
                            )
                        })
                    }
                </tbody>
            </Table>
            <Button onClick={stopStreaming}>Stop</Button>
            {/* {stringArray[0]} */}
            {/* {stringArray ? stringArray.map((message, index) => <p key={index}>{message}</p>) : <p>Loading...</p>} */}
        </>
    );
}

export default GetData;
