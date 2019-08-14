import React, { useState } from 'react';
import { useObservable } from 'rxjs-hooks';
import { Observable } from 'rxjs';
import { map, withLatestFrom } from 'rxjs/operators';
import { Table } from 'reactstrap';
// import { ReactTable } from 'react-table';

const url = "http://localhost:8080/streamTime/sse";
const stringObservable = Observable.create(observer => {
    const source = new EventSource(url);
    source.addEventListener('message', (messageEvent) => {
        // console.log(messageEvent);
        observer.next(messageEvent.data);
    }, false);
});

function GetData() {
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

    return (
        <>
            {/* <ReactTable>
            columns = { columns }
            resolveData = {data => data.map(row => row)}
        </ReactTable> */}
            <Table responsive>
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
                            // message = message.replace(/'/g, '"')
                            console.log("after " + message)
                            // message = JSON.parse(message)
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
            {/* {stringArray[0]} */}
            {/* {stringArray ? stringArray.map((message, index) => <p key={index}>{message}</p>) : <p>Loading...</p>} */}
        </>
    );
}

export default GetData;
