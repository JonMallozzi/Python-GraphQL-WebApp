import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { fetchUser } from '../../controllers/userController';

export const Login: React.FC = () => {
    const history = useHistory();
    let [username, setUsername] = useState<string>('');
    let [password, setPassword] = useState<string>('');

    const submit = (e: any) => {
        e.preventDefault();
        console.log(fetchUser(username, password));
        history.push("/");
    };

    return (
       <form onSubmit={submit}>
           <label>
                Username:
            <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
           </label>
           <label>
                Password:
            <input type="text" value={password} onChange={e => setPassword(e.target.value)} />
           </label>
           <input type="submit" value="Submit" />
       </form>
    );
};