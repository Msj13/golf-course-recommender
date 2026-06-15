import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { House } from 'lucide-react';
import './Dashboard.css';

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const userResponse = await fetch('http://localhost:8000/users/1');
        const userData = await userResponse.json();
        setUser(userData);
  
        const statsResponse = await fetch('http://localhost:8000/users/1/stats');
        const statsData = await statsResponse.json();
        setStats(statsData);
  
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };
  
    fetchData();
  }, []);
  
  if (loading) return <div className="loading">Loading...</div>;
  
  return (
    <div className="dashboard">

      <div className='welcome-message'>
        <h1>Welcome back, {user.name}</h1>
        <p>Here's how your game is trending this season.</p>
      </div>
      {user && (
        <div className="user-card">
          <Link to="/profile" style={ {textDecoration: 'none'} }>
            <div className="avatar">
              <p>{user.name.split(" ").map(word => word[0]).join("").slice(0, 2)}</p>
            </div>
          </Link>
          <h2>{user.name}</h2>
          <div>{user.home_location}</div>
          <div className="user-info">
            <div>
              <p className="label">Handicap</p>
              <p className="value">{user.handicap}</p>
            </div>
            <div>
              <p className="label">Email</p>
              <p className="value">{user.email}</p>
            </div>
          </div>
        </div>
      )}
      
      {stats && (
        <div className="stats-card">
          <h3>Your Stats</h3>
          <div className="stats-grid">
            <div className="stat-box stat-blue">
              <p className="label">Rounds Played</p>
              <p className="value">{stats.rounds_played}</p>
            </div>
            <div className="stat-box stat-green">
              <p className="label">Average Score</p>
              <p className="value">{stats.avg_score}</p>
            </div>
            <div className="stat-box stat-purple">
              <p className="label">Best Score</p>
              <p className="value">{stats.best_score}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}