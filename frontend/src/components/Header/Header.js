import styles from './Header.css'


export default function Header() {
    return (
        <header style={styles}>
            <p className="logo">header</p>
            <a href='account.html'>
                <p className="account">
                    account
                </p>
            </a>
        </header>
    );
}