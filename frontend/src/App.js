import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import RoundsTable from './components/RoundsTable';
import RoundDetail from './components/RoundDetail';
import Profile from './components/Profile';


function App() {
  return (
    <Router>
      <header>
        <h1>⛳ Golf Dashboard</h1>
        <p>Track your rounds, get recommendations</p>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/rounds" element={<RoundsTable userId={10}/>} />
          <Route path="/rounds/:roundId" element={<RoundDetail/>} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;