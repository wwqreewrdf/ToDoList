import styles from './Header.css'

export default function Header() {
    return (
        <header style={styles}>
            <p class="logo">header</p>
            <a href='account.html'>
                <p class="account">
                    account
                </p>
            </a>

        </header>
    );
}