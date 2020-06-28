import React, {useState, createContext, useContext } from 'react';

export const UserContext = createContext<object>({});

export const UserProvider = (props: any) => {
    const [user, setUser] = useState<
    {
        username: string,
        password: string,
        email: string,
        dateCreated: any,
        dateOfBirth: any
    }
    >(
       {
        username: 'Login', 
        password: '', 
        email: '', 
        dateCreated: '', 
        dateOfBirth: ''
       }
    );

    return (
        <UserContext.Provider value={[user, setUser]}>
            {props.children}
        </UserContext.Provider>
    );
};

export const UserConsumer = () => useContext(UserContext);