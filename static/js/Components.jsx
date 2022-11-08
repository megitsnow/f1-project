function SignUpForm(props) {
    const {formData, handleChange, handleSubmit} = props;
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

function LogIn(props) {
    const {logInData, handleLogInChange, handleLogInSubmit} = props;
    return (
        <div>
        <form className="form" onSubmit={handleLogInSubmit}>
            <input 
                type="email" 
                placeholder="Email address"
                name="email"
                onChange={handleLogInChange}
                value={logInData.email}
            />
            <input 
                type="password" 
                placeholder="Password"
                name="password"
                onChange={handleLogInChange}
                value={logInData.password}
            /> 
            <ReactRouterDOM.Link to="/sign-up">Not A User? Sign Up</ReactRouterDOM.Link>    
            <button>
                Sign In
            </button>
        </form>
    </div>
    );
    }


function Homepage(props) {
    return (
        <div>
            <p>Homepage</p>
        </div>
    );
}