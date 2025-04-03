// const pokemons = ["皮卡丘", "杰尼龟", "小火龙", "妙蛙种子"];

/*
class App extends React.Component {
    constructor() {

        console.log("构造函数")

        super();
        this.state = {
            // pokemons: ["皮卡丘", "杰尼龟", "小火龙", "妙蛙种子"],
            pokemons: [],
            // egg: "RzMY"
            searching: "",
            filteredPokemons: []
        };
    }

    componentDidMount() {

        console.log("组件挂载")

        fetch('https://pokeapi.co/api/v2/pokemon')
            .then(res => res.json())
            .then(json => {
                // this.setState({
                //     pokemons: json.results
                // });// 异步后执行
                // console.log(this.state);
                json.results.map((results, index) => {
                    results.id = index + 1;
                })
                this.setState(
                    () => {
                        return {
                            pokemons: json.results,
                            filteredPokemons: json.results
                        }
                    },
                    () => {
                        console.log(this.state);
                    }
                )// 浅合并
            });
    }

    onChangeHandler = event => {
        const comparedPokemons = this.state.pokemons.filter(
            pokemons => {
                return pokemons.name.includes(event.target.value)
            }
        )

        this.setState(
            () => {
                return {
                    filteredPokemons: comparedPokemons,
                }
            },
            () => {
                console.log(this.state.searching)
            }
        )
    }

    render() {

        console.log("渲染")

        return (
            <div>
                <h1>Hello,React!</h1>
                <Input onChangeHandler = { this.onChangeHandler }/>
                <Lists pokemonsLists = { this.state.filteredPokemons }/>
            </div>
        );
    }
}
*/

const App = () => {
    const [pokemons, setPokemons] = React.useState([]);
    const [filteredPokemons, setFilteredPokemons] = React.useState([]);

    React.useEffect(
        () => {
            fetch('https://pokeapi.co/api/v2/pokemon')
            .then(res => res.json())
            .then(json => {
                json.results.map((results, index) => {
                    results.id = index + 1;
                })
                setPokemons(json.results);
                setFilteredPokemons(json.results);
            });
        },
        [] // 只执行一次
    )

    const onChangeHandler = event => {
        const comparedPokemons = pokemons.filter(
            pokemons => {
                return pokemons.name.includes(event.target.value)
            }
        )
        setFilteredPokemons(comparedPokemons);
    }

    return (
        <div>
            <h1>Hello,React!</h1>
            <Input onChangeHandler = { onChangeHandler }/>
            <Lists pokemonsLists = { filteredPokemons }/>
        </div>
    )
}