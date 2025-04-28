import styles from './LeftMenu.css'
import React, { useState, useEffect } from 'react';

export default function LeftMenu() {

    const [users, setUsers] = useState([])

    const fetchData = () => {
        fetch("http://127.0.0.1:8000/todo/table")
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
            sidebar test
            
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