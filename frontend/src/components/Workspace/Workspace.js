import styles from './Workspace.css'
import Group from '../Group/Group'
import React, { useState, useEffect } from 'react';

export default function Workspace() {

    const [users, setUsers] = useState([])
    
    const fetchData = () => {
        fetch("http://127.0.0.1:8000/table/id")
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
        <main style={styles}>
            <p>workspace</p>
            {users.length > 0 && (
                <ul>
                    {users.map(user => (
                        <li key={user.id}>{user.id} {user.name}</li>
                    ))}
                </ul>
            )}
            <Group />
            <Group />
        </main>
    );
}