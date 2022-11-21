
// Things to work on: Are there ways to re-use some of this code?
// For example, some of functions are very similar like the ones for the 
// login and sign up forms. Additionally, I need to look at the naming and make 
// sure that everything is intuitive 

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
            to="/user-profile">
            <h3>User Profile</h3>
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

function UserProfile(props) {
    return (
        <div>
            <p>User Profile</p>
        </div>
    );
}

// Drivers

function Drivers(props) {
    const {activeDriverData} = props
    const activeDriverCards = [];

    for (const driver of Object.values(activeDriverData)) {
      const driverCard = (
        <DriverCard
          key={driver.code}
          surname = {driver.surname}
          img = {driver.img_url}
          nationality = {driver.nationality}
          id = {driver.driver_id}
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
    const { surname, img, nationality, id} = props;

   const driverInformation= {}
   driverInformation['driverId'] = id


    function addToLikes() {
        alert("clicked!")
        fetch('/api/driver-like', {
            method: 'POST',
            body: JSON.stringify(driverInformation),
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
            <ReactRouterDOM.Link to={`/drivers/${id}`}><img src = {img}/></ReactRouterDOM.Link>
            <h2>{surname}</h2>
            <h1>{nationality}</h1>
            <img src = '/static/imgs/drivers/hearticon.jpeg' onClick = {addToLikes}></img>
        </div>

    );
}

function DriverDetails(props) {
    const params = ReactRouterDOM.useParams()
    const [driverInfo, setDriverInfo] = React.useState({});
    const driverId = params.driverId
    let count = 0

    const url = `/drivers/${driverId}`;

    React.useEffect(() => {
    fetch(url)
        .then((response) => response.json())
        .then((driverData) => {
        setDriverInfo(driverData);
        });
    }, []);

    const resultsDriverCards = []

    for (const driver of Object.values(driverInfo)) {
        const resultCard = (
          <DriverResultCard
            key={`${driver.race_name}${driver.fname}${count}`}
            points = {driver.points}
            position = {driver.position}
            race_name = {driver.race_name}
          />
        );
        count++
        resultsDriverCards.push(resultCard);
      }


    return (
        <div>
            <table>
            <tr>
                <th>Race Name</th>
                <th>Points</th>
                <th>Position</th>
            </tr>
            {resultsDriverCards}
            </table>
        </div>
        );
    }

    function DriverResultCard(props) {
        const { points, position, race_name} = props;
        return (
            <tr>
                <td>{race_name}</td>
                <td>{position}</td>
                <td>{points}</td>
            </tr>
    
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
        </div>

    );
}

function ConstructorDetails(props) {
    const params = ReactRouterDOM.useParams()
    const [constructorInfo, setConstructorInfo] = React.useState({});

    const constructorId = params.constructorId
    const url = `/constructors/${constructorId}`;

    React.useEffect(() => {
        fetch(url)
            .then((response) => response.json())
            .then((constructorData) => {
            setConstructorInfo(constructorData);
            });
        }, []);
        
        const individualConstructorCard = (
            <IndividualConstructorCard
            img = {constructorInfo.img}
            name = {constructorInfo.name}
            nationality = {constructorInfo.nationality}
            wiki_url = {constructorInfo.wiki_url}
            />
        );


    return (
        <div>
            <img src = {constructorInfo.img}/>
            {individualConstructorCard}
        </div>
    );
}

function IndividualConstructorCard(props) {
    const { img, name, nationality, wiki_url} = props;
    return (
        <div>
            <h3>{name}</h3>
            <h2>Nationality - {nationality}</h2>
            <a href={wiki_url} target="_blank">History of {name}</a>
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
            url_to_image = {article.url_to_img}
            />
        );
        count++
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