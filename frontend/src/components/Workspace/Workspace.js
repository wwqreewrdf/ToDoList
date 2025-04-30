import styles from './Workspace.css'
import Group from '../Group/Group'
import React, { useState, useEffect } from 'react';


export default function Workspace() {
    return (
        <main style={styles}>
            <p>workspace</p>
            <ul>
                element
            </ul>
            <Group />
            <Group />
        </main>
    );
}