/*
class Input extends React.Component {
    render() {
        const { onChangeHandler } = this.props;
        return (
            <input type="search" onChange = { onChangeHandler }/>
        )
    }
}
*/
const Input = ({ onChangeHandler }) => {
    return (
        <input type="search" onChange = { onChangeHandler }/>
    )
}