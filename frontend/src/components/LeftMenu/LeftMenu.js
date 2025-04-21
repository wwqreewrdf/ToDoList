import styles from './LeftMenu.css'
import React, { useState, useEffect } from 'react';

export default function LeftMenu() {

    const [users, setUsers] = useState([])

    const fetchData = () => {
        fetch("https://jsonplaceholder.typicode.com/users")
            .then(response => {
                return response.json()
            })
            .then(data => {
                setUsers(data)
            })
    }

    useEffect(() => {
        fetchData()
    }, [])

    return (
        <aside style={styles} id="sidebar">
            {users.length > 0 && (
                <ul>
                    {users.map(user => (
                        <li key={user.id}>{user.id} {user.name}</li>
                    ))}
                </ul>
            )}
        </aside>
    );
}