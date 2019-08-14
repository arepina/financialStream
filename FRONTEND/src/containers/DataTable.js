import React,{ Component, useState }  from 'react';
import { Table } from 'reactstrap';
import { useObservable } from 'rxjs-hooks';
import { Observable } from 'rxjs';
import { map, withLatestFrom } from 'rxjs/operators';
import GetData from './GetData';

// const stringObservable = Observable.create(observer => {
//    let url = "http://localhost:8080/streamTime/sse";
//    const source = new EventSource(url);
//    source.addEventListener('message', (messageEvent) => {
//      console.log(messageEvent);
//      observer.next(messageEvent.data);
//    }, false);
//  });

// const DataTableFn = props => {

//    const [data, setData] = useState([
//       [
//          { id: 1, instrumentName: 'Wasif', cpty: 21, price: 'wasif@email.com',
//            type: '123', quantity: '1', time: '1' },
//     //      { id: 2, name: 'Ali', age: 19, email: 'ali@email.com' },
//     //      { id: 3, name: 'Saad', age: 16, email: 'saad@email.com' },
//     //      { id: 4, name: 'Asad', age: 25, email: 'asad@email.com' }
//     ]
//    ]);

//    useObservable(
//       state =>
//         stringObservable.pipe(
//           withLatestFrom(state),
//           map(([state]) => {
//             let updatedData = data;
//             updatedData.unshift(state);
//             if (updatedData.length >= 50) {
//               updatedData.pop();
//             }
//             setData(updatedData);
//             return state;
//           })
//         )
//     );

//     return (
//       <>
//         {data[0]}
//         {/* {stringArray ? stringArray.map((message, index) => <p key={index}>{message}</p>) : <p>Loading...</p>} */}
//       </>
//     );
// }

export default class DataTable extends Component {
    constructor(props) {
       super(props) 
       this.state = { 
           data: [
             { id: 1, instrumentName: 'Wasif', cpty: 21, price: 'wasif@email.com',
               type: '123', quantity: '1', time: '1' },
        //      { id: 2, name: 'Ali', age: 19, email: 'ali@email.com' },
        //      { id: 3, name: 'Saad', age: 16, email: 'saad@email.com' },
        //      { id: 4, name: 'Asad', age: 25, email: 'asad@email.com' }
        ]
       }
      }

    renderTableData() {
        return this.state.data.map((data, index) => {
           const { id, instrumentName, cpty, price, type, quantity, time } = data
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
      // <Table responsive>
      //   <thead>
      //     <tr>
      //       <th>#</th>
      //       <th>instrumentName</th>
      //       <th>cpty</th>
      //       <th>price</th>
      //       <th>type</th>
      //       <th>quantity</th>
      //       <th>time</th>
      //     </tr>
      //   </thead>
      //   <tbody>
      //     {this.renderTableData()}
      //   </tbody>
      // </Table>
      <GetData/>
    );
  }
}