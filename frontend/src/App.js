import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import RoundsTable from './components/RoundsTable';
import RoundDetail from './components/RoundDetail';
import Profile from './components/Profile';
import NavBar from './components/NavBar'


function App() {
  return (
    <Router>

      <NavBar/>

      <main>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/rounds" element={<RoundsTable userId={10}/>} />
          <Route path="/rounds/:roundId" element={<RoundDetail/>} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;