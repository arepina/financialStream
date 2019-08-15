import React, { useState } from 'react';
import { useObservable } from 'rxjs-hooks';
import { Observable } from 'rxjs';
import { map, withLatestFrom, filter } from 'rxjs/operators';
import { Table, Input, Button } from 'reactstrap';
import "./TableData.css";
import baseUrl from "./Utils";

    const url = baseUrl + '/streamTime/sse';
    const source = new EventSource(url);
    const stringObservable = Observable.create(observer => {
        source.addEventListener('message', (messageEvent) => {
            // console.log(messageEvent);
            observer.next(messageEvent.data);
        }, false);
    });
    
function TableData() {
    const myTable = "myTable";

    const [stringArray, setStringArray] = useState([]);
    const refresh = event => {
        window.location.reload();
    }

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

    const stopStreaming = event => {
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

        if (filter) {
            // Loop through all table rows, and hide those who don't match the search query
            for (i = 1; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[1];
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    // if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    if (txtValue.toUpperCase() === filter) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";
                    }
                }
            }
        }
        else {
            for (i = 1; i < tr.length; i++) {
                    tr[i].style.display = "";
                }
            }
    }

    return (
        <>
            <Input type="text" id="myFilter" onKeyPress={filterFn} placeholder="Filter for Instrument here..."></Input>
            <div id="table-wrapper">
            <div id="table-scroll">
            <Table responsive id={myTable}>
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
                    {
                        stringArray.map((message, index) => {
                            message = message.replace(/'/g, '"')
                            message = JSON.parse(message)
                            return (
                                <tr key={index}>
                                <td>{index}</td>
                                <td>{message.instrumentName}</td>
                                <td>{message.cpty}</td>
                                <td>{message.price}</td>
                                <td>{message.type}</td>
                                <td>{message.quantity}</td>
                                <td>{message.time}</td>
                                </tr>
                            )
                        })
                    }
                </tbody>
            </Table>
            </div>
            </div>
            <Button onClick={stopStreaming}>Stop</Button>
            <Button onClick={refresh}>Refresh</Button>
        </>
    );
}

export default TableData;
