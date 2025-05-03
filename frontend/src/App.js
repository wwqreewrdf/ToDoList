import Header from './components/Header/Header';
import LeftMenu from './components/LeftMenu/LeftMenu';
import Workspace from './components/Workspace/Workspace';
import Footer from './components/Footer/Footer';

import styles from './index.css'


function getCookie(name) {
    var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function refresh_check() {
    var refresh = getCookie("refresh");
    console.log(refresh)
    fetch('http://127.0.0.1:8000/user/refresh', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "refresh": refresh
        })
    })
        .then(res => res.json())
        .then((data) => {
            if (data["code"] == "token_not_valid") {
                window.location = 'http://127.0.0.1:3000/account.html'
                console.log("refresh_token_not_valid")
            } else {
                localStorage.setItem('access', data["access"]);
                document.cookie = `refresh=${data["refresh"]};`;
                window.location.reload();
            };
        })
}

function access_check() {
    var access = localStorage.getItem('access');
    if (access == null) {
        window.location = 'http://127.0.0.1:3000/account.html'
    }
    fetch('http://127.0.0.1:8000/user/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "token": access
        })
    })
        .then(res => res.json())
        .then((data) => {
            if (data["code"] == "token_not_valid") {
                console.log("access_token_not_valid: checking refsresh")
                refresh_check()
            }
        })
}

export default function App() {

    access_check();

    return (
        <div className="App" style={styles}>
            <Header />
            <LeftMenu />
            <Workspace />
            <Footer />
        </div>
    );
}