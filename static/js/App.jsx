function App () {   
    
    const [constructorData, setConstructorData] = React.useState({});
    const [activeDriverData, setActiveDriverData] = React.useState({});
    const [recentNewsData, setRecentNewsData] = React.useState([]);

    React.useEffect(() => {
        fetch('/api/constructors')
            .then((response) => response.json())
            .then((constructorLogoData) => {
            setConstructorData(constructorLogoData);
            });
        }, []);


    React.useEffect(() => {
        fetch('/api/active_drivers')
            .then((response) => response.json())
            .then((activeDriverData) => {
            setActiveDriverData(activeDriverData);
            });
        }, []);

    React.useEffect(() => {
        fetch('/api/recent-news')
            .then((response) => response.json())
            .then((recentNewsData) => {
            setRecentNewsData(recentNewsData);
            });
        }, []);


    return (
    <div>
        <ReactRouterDOM.BrowserRouter>
        <Navbar logo="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" brand="F1" />
            
            <ReactRouterDOM.Route exact path="/log-in">
                <LogIn/>
            </ReactRouterDOM.Route>

            <ReactRouterDOM.Route exact path="/sign-up">
                <SignUpForm />
            </ReactRouterDOM.Route >

            <ReactRouterDOM.Route exact path="/">
                <HomePage/>
            </ReactRouterDOM.Route>

            <ReactRouterDOM.Route exact path="/user-profile">
                <UserInformation/>
                <UserProfile/>
                {/* <CloudinaryUpload/> */}
            </ReactRouterDOM.Route>

            <ReactRouterDOM.Route exact path="/drivers">
                <Drivers activeDriverData = {activeDriverData}/>
            </ReactRouterDOM.Route >

            <ReactRouterDOM.Route path="/drivers/:driverId">
                <DriverDetails/>
            </ReactRouterDOM.Route >

            <ReactRouterDOM.Route exact path="/constructors">
                <Constructors constructorData = {constructorData}/>
            </ReactRouterDOM.Route >

            <ReactRouterDOM.Route path="/constructors/:constructorId">
                <ConstructorDetails/>
            </ReactRouterDOM.Route >
            
            <ReactRouterDOM.Route exact path="/recent-news">
                <RecentNews recentNewsData = {recentNewsData}/>
            </ReactRouterDOM.Route >
        </ReactRouterDOM.BrowserRouter>
    </div>  
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));