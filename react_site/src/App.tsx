import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Homepage } from './Components/Homepage/homepage';
import './App.css';
import { Login } from './Components/Login/login';
import { UserProvider } from './Context/userContext';
import { Header } from './Components/Header/header';

const App: React.FC = () =>{
  return (
    <UserProvider>
      <Router>
        <div className="App">
          <Header/>
          <Switch>
            <Route path={'/'} exact component={Homepage}/>
            <Route path={'/login'} exact component={Login}/>
          </Switch>
        </div>
      </Router>
    </UserProvider>
   );
}

export default App;
