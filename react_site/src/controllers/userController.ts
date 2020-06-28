import axios from "axios";


 //get request
export const fetchUser = async(username: string, password: string) => {
    try {
        const result = await axios({
            method: "POST",
            url: "http://localhost:8000/graphql/",
            data: {
                query: `
                    query getUserbyUsername{
                        userByUsername(username: "${username}"){
                        id
                        username
                        password
                      }
                  }
                `
            },
        });
        if(password === result.data.data.userByUsername.password){
            alert(`Correct login info for: ${username}`);
            
        }
    } catch (error) {
        console.error(error);
        alert('Incorrect username or password');
    }
    finally{
        getUsername(username);
    }
}

//callback function to get the username once the user is fetched
const getUsername = (username: string): string => {
    return username;
}