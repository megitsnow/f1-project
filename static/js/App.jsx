function App () {
    const [logInUser, setlogInUser] = React.useState("");

    React.useEffect(() => {
        fetch('/handle_login', {
            method: 'POST',
        })
            .then((response) => response.json())
            .then((result) => {
            setlogInUser(result)
            });
        }, []);

    return (
    <div>
        {logInUser ? <Welcome/> : <Login/>}
    </div>  
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));