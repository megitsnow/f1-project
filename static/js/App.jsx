function App () {
    const[logIn, setLogIn] = React.useState(false);
    const[signUp, setSignUp] = React.useState(false);

    const [logInData, setLogInData] = React.useState({
        email: "",
        password: "",
    })

    const [formData, setFormData] = React.useState({
        fname: "",
        lname: '',
        email: "",
        password: "",
        passwordConfirm: "",
    })
    
    function handleLogInChange(event) {
        const {name, value} = event.target
        setFormData(prevLogInData => ({
            ...prevLogInData,
            [name]: value
        }))
    }

    function handleChange(event) {
        const {name, value} = event.target
        setLogIn(prevFormData => ({
            ...prevFormData,
            [name]: value
        }))
    }
    
    function handleSubmit(event) {
        event.preventDefault()
        if(formData.password === formData.passwordConfirm) {
            alert("Successfully signed up")
            setSignUp(true)
            React.useEffect(() => {
                fetch('/api/sign-up', {
                    method: 'POST',
                    body: JSON.stringify(logInData),
                    headers: {
                    'Content-Type': 'application/json',
                    },
                })
                    .then((response) => response.json())
                    .then((responseJson) => {
                    alert(responseJson.status);
                    });
                }, []);
        } else {
            alert("Passwords do not match")
            return
        } }

    function handleLogInSubmit(event) {
        event.preventDefault()
        if(formData.password === 'hello') {
            alert("Successfully logged in")
            setLogIn(true)
        } else {
            alert("Passwords do not match")
            return
        } }
        

    return (
    <div>
        <ReactRouterDOM.BrowserRouter>
            <ReactRouterDOM.Route exact path="/">
                <LogIn logInData = {logInData} handleLogInChange = {handleLogInChange} handleLogInSubmit = {handleLogInSubmit}/>
            </ReactRouterDOM.Route>
            <ReactRouterDOM.Route exact path="/sign-up">
                <SignUpForm formData = {formData} handleChange = {handleChange} handleSubmit = {handleSubmit}/>
            </ReactRouterDOM.Route>
            {/* <ReactRouterDOM.Route exact path="/homepage">
                {logIn ? <Homepage/> : <ReactRouterDOM.Redirect to="/login"/> }
            </ReactRouterDOM.Route> */}
        </ReactRouterDOM.BrowserRouter>
    </div>  
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));

