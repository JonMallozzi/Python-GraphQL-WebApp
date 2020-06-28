import React from 'react';
import { Link } from 'react-router-dom';
import { UserConsumer } from '../../Context/userContext';
import './header.css';


export const Header: React.FC = () => {
    const userContext = UserConsumer();
    return(
        <div>
          <Link to="/" className="Home">Home</Link>
          <Link to="/login" className="Login">{Object.values(userContext)[0].username}</Link>
        </div>
    );
};