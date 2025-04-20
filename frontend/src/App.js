import Header from './components/Header/Header';
import LeftMenu from './components/LeftMenu/LeftMenu';
import Workspace from './components/Workspace/Workspace';

import styles from './index.css'

export default function App() {
  return (
    <div class="App" style={styles}>
        <Header />
        <LeftMenu />
        <Workspace />
    </div>
  );
}