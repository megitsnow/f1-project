function Login(props) {
    return (
        <div className = "login-form">
            <form action="/handle_login" method="POST"/>
            <label>Username:</label>
            <input type="text" name="email" className = "login-form"/>

            <label>Password:</label>
            <input type="text" name="password" className = "login-form"/>

            <input type="submit"/>
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