
// Sign Up Form

function SignUpForm(props) {
    const [formData, setFormData] = React.useState({
        fname: "",
        lname: '',
        email: "",
        password: "",
        passwordConfirm: "",
    })

    const handleChange = (event) => {
        console.log(formData)
        const {name, value} = event.target
        setFormData(prevFormData => ({
            ...prevFormData,
            [name]: value
        }))
        console.log(formData)
    }
    const handleSubmit = (event) => {
        event.preventDefault()
        fetch('/api/sign-up', {
            method: 'POST',
            body: JSON.stringify(formData),
            headers: {
            'Content-Type': 'application/json',
            },
        })
            .then((response) => response.json())
            .then((responseJson) => {
            alert(responseJson.status);
            });
    }
    return (
        <div>
        <form className="form" onSubmit={handleSubmit}>
            <input 
                type="text" 
                placeholder="First Name"
                name="fname"
                onChange={handleChange}
                value={formData.fname}
            />
            <input 
                type="text" 
                placeholder="Last Name"
                name="lname"
                onChange={handleChange}
                value={formData.lname}
            />
            <input 
                type="email" 
                placeholder="Email address"
                name="email"
                onChange={handleChange}
                value={formData.email}
            />
            <input 
                type="password" 
                placeholder="Password"
                name="password"
                onChange={handleChange}
                value={formData.password}
            />
            <input 
                type="password" 
                placeholder="Confirm password"
                name="passwordConfirm"
                onChange={handleChange}
                value={formData.passwordConfirm}
            />
            
            <button>
                Sign up
            </button>
        </form>
    </div>
    );
    }

// LogIn Form

function LogIn(props) {

    const [logInData, setLogInData] = React.useState({
        email: "",
        password: "",
    })

    const handleChange = (event) => {
        console.log("Line 93 Log in", logInData)
        const {name, value} = event.target
        setLogInData(prevLogInData => ({
            ...prevLogInData,
            [name]: value
        }))
        console.log(logInData)
    }
    const handleSubmit = (event) => {
        event.preventDefault()
        fetch('/api/log-in', {
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
    }

    return (
        <div>
        <form className="form" onSubmit={handleSubmit}>
            <input 
                type="email" 
                placeholder="Email address"
                name="email"
                onChange={handleChange}
                value={logInData.email}
            />
            <input 
                type="password" 
                placeholder="Password"
                name="password"
                onChange={handleChange}
                value={logInData.password}
            /> 
            <ReactRouterDOM.Link to="/sign-up">Not A User? Sign Up</ReactRouterDOM.Link>    
            <button>Log In</button>
        </form>
    </div>
    );
    }

// Navbar

function Navbar(props) {
    const { logo, brand } = props;

return (
    <nav>
    <section className = "nav-bar">
        <ReactRouterDOM.Link to="/">
            <img src={logo} height="30" alt="logo" />
        </ReactRouterDOM.Link>

        <ReactRouterDOM.NavLink
            to="/drivers">
            <h3>Drivers</h3>
        </ReactRouterDOM.NavLink>

        <ReactRouterDOM.NavLink
            to="/constructors">
            <h3>Constructors</h3>
        </ReactRouterDOM.NavLink>

        <ReactRouterDOM.NavLink
            to="/recent-news">
            <h3>Recent News</h3>
        </ReactRouterDOM.NavLink>

        <ReactRouterDOM.NavLink
            to="/log-in">
            <h3>Log In</h3>
        </ReactRouterDOM.NavLink>
    </section>
    </nav>
    );
}

// Homepage

function HomePage(props) {
    return (
        <div>
            <p>Homepage</p>
        </div>
    );
}

// Drivers

function Drivers(props) {
    const {activeDriverData} = props
    // same as saying const constructordata = props.constructordata
    const activeDriverCards = [];

    for (const driver of Object.values(activeDriverData)) {
        console.log(driver)
      const driverCard = (
        <DriverCard
          key={driver.code}
          surname = {driver.surname}
          img = {driver.img_url}
          nationality = {driver.nationality}
        />
      );
  
      activeDriverCards.push(driverCard);
    }
    return (
        <div>
            {activeDriverCards}
        </div>
        
    );
}

function DriverCard(props) {
    const { surname, img, nationality} = props;
    return (
        <div>
            <img src = {img}/>
            <h2>{surname}</h2>
            <h1>{nationality}</h1>
        </div>

    );
}

// Constructors

function Constructors(props){
    const {constructorData} = props
    const constructorCards = [];

    for (const constructor of Object.values(constructorData)) {
      const constructorCard = (
        <ConstructorCard
          key={constructor.constructor_api_ref}
          name = {constructor.name}
          img = {constructor.img}
          id = {constructor.constructor_id}
        />
      );
  
      constructorCards.push(constructorCard);
    }
    return (
        <div>
            {constructorCards}
        </div>
        
    );
}

function ConstructorCard(props) {
    const { name, img, id} = props;
    return (
        <div>
            <ReactRouterDOM.Link to={`/constructors/${id}`}><img src = {img}/></ReactRouterDOM.Link>
            <h2>{name}</h2>
        </div>

    );
}

function ConstructorDetails(props) {
    const params = ReactRouterDOM.useParams()
    const [constructorInfo, setConstructorInfo] = React.useState({});
    console.log(params)
    const constructorId = params.constructorId
    console.log(constructorId)
    const queryString = new URLSearchParams({ constructorId: {constructorId} }).toString();
    const url = `/constructors/?${queryString}`;

    React.useEffect(() => {
        fetch(url)
            .then((response) => response.json())
            .then((constructorData) => {
            setConstructorInfo(constructorData);
            });
        }, []);

    return (
        <div>
            <h1>Constructor Details</h1>
        </div>
    );
}

// Recent News

function RecentNews(props){
    const {recentNewsData} = props
    const newsCards = [];
    let count = 0

    for (const article of Object.values(recentNewsData)) {
        const newsCard = (
            <NewsCard
            key={`article${count}`}
            description = {article.description}
            title = {article.title}
            url = {article.url}
            url_to_image = {article.url_to_image}
            />
        );
        count++
        console.log(count)
        newsCards.push(newsCard);
    }
    return (
        <div>
            {newsCards}
        </div>
        
    );
}

function NewsCard(props) {
    const { description, title, url, url_to_image} = props;
    return (
        <div>
            <img src = {url_to_image}/>
            <a href={url} target="_blank">{title}</a>
            <h1>{description}</h1>
        </div>

    );
}