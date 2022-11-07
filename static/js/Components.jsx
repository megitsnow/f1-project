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

function Homepage(props) {
    return (
        <div>
            <p>Homepage</p>
        </div>
    );
}