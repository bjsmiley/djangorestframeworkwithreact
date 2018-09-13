import React from 'react'
import PropTypes from 'prop-types'

class DataProvider extends React.Component{
    
    static propTypes = {
        endpoint: PropTypes.string.isRequired,
        render: PropTypes.func.isRequired
    };

    state = {
        data: [],
        loaded: false,
        placeholder: "Loading..."
    };

    componentDidMount(){
        fetch( this.props.endpoint ).then(response => {
            if( response.status !== 200){
                return this.setState({placeholder: "Error: Something went wrong"})
            }
            return response.json()
        }).then( data => this.setState({ data: data.results, loaded: true }))
    }

    render(){
       return this.state.loaded ? this.props.render(this.state.data) : <p>{this.state.placeholder}</p>; // if the data is loaded correctly, call the render method which will create the table
    }
}

export default DataProvider;