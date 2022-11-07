function App () {
    const [formData, setFormData] = React.useState({
        fname: "",
        lname: '',
        email: "",
        password: "",
        passwordConfirm: "",
    })
    
    function handleChange(event) {
        const {name, value} = event.target
        setFormData(prevFormData => ({
            ...prevFormData,
            [name]: value
        }))
    }
    
    function handleSubmit(event) {
        event.preventDefault()
        if(formData.password === formData.passwordConfirm) {
            alert("Successfully signed up")
        } else {
            alert("Passwords do not match")
            return
        } }
        

    return (
    <div>
        <Login formData = {formData} handleChange = {handleChange} handleSubmit = {handleSubmit}/> 
    </div>  
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));