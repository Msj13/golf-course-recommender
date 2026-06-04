import { useState, useEffect } from 'react';
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
      <h1>Golf Dashboard</h1>
      
      {user && (
        <div className="user-card">
          <h2>{user.name}</h2>
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