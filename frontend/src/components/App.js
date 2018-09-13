import React from "react";
import ReactDOM from "react-dom";

import DataProvider from './DataProvider'
import Table from './Table'


const App = () => (
    <DataProvider endpoint='api/snippets/' render={ data => <Table data={data}/> } /> // render is a function that takes param @data and creates the table component with it

)


const container = document.getElementById('app')
ReactDOM.render(
    <App/>,
    container
)