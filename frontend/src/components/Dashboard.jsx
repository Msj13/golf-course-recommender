import { useState, useEffect } from 'react';

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
  
  if (loading) return <div className="p-8">Loading...</div>;
  
  return (
    <div className="p-8 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold mb-8">Golf Dashboard</h1>
      
      {user && (
  <div className="bg-white rounded-lg shadow-lg p-8 mb-8 border-l-4 border-green-600">
    <h2 className="text-3xl font-bold text-gray-800 mb-4">{user.name}</h2>
    <div className="grid grid-cols-2 gap-4">
      <div>
        <p className="text-gray-600 text-sm uppercase tracking-wide">Handicap</p>
        <p className="text-2xl font-bold text-green-600">{user.handicap}</p>
      </div>
      <div>
        <p className="text-gray-600 text-sm uppercase tracking-wide">Email</p>
        <p className="text-lg text-gray-800">{user.email}</p>
      </div>
    </div>
  </div>
)}
      
      {stats && (
  <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
    <h3 className="text-2xl font-bold text-gray-800 mb-6">Your Stats</h3>
    <div className="grid grid-cols-3 gap-6">
      <div className="bg-blue-50 p-6 rounded-lg border-t-4 border-blue-500">
        <p className="text-gray-600 text-sm mb-2">Rounds Played</p>
        <p className="text-4xl font-bold text-blue-600">{stats.rounds_played}</p>
      </div>
      <div className="bg-green-50 p-6 rounded-lg border-t-4 border-green-500">
        <p className="text-gray-600 text-sm mb-2">Average Score</p>
        <p className="text-4xl font-bold text-green-600">{stats.avg_score}</p>
      </div>
      <div className="bg-purple-50 p-6 rounded-lg border-t-4 border-purple-500">
        <p className="text-gray-600 text-sm mb-2">Best Score</p>
        <p className="text-4xl font-bold text-purple-600">{stats.best_score}</p>
      </div>
    </div>
  </div>
)}
    </div>
  );
}