import { useState, useEffect } from 'react';
import './Profile.css';

export default function Profile() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [homeLocation, setHomeLocation] = useState('');
  const [budget, setBudget] = useState('');
  const [travelRadius, setTravelRadius] = useState('');

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const res = await fetch('http://localhost:8000/users/1');
        const data = await res.json();
        setUser(data);
        setLoading(false);
        setHomeLocation(data.home_location || '');
        setBudget(data.budget_per_round || '');
        setTravelRadius(data.travel_radius_miles || '');

      } catch (error) {
        console.error('Error fetching user:', error);
        setLoading(false);
      }
    };

    fetchUser();
  }, []);


  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch('http://localhost:8000/users/1', {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        home_location: homeLocation,
        budget_per_round: parseFloat(budget),
        travel_radius_miles: parseInt(travelRadius),
      }),
    });

    const data = await res.json();
    setUser(data);
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div className="profile">
      {/* TODO: render avatar with initials here */}

      <h2>Edit Profile</h2>

      <form onSubmit={handleSubmit}>
        <div>
          <p>Change Budget</p>
          <input type="text" value={budget} onChange={(e) => setBudget(e.target.value)}/>
        </div>
        <div>
          <p>Location</p>
          <input type="text"  value={homeLocation} onChange={(e) => setHomeLocation(e.target.value)}/>
        </div>
        <div>
          <p>Max Travel Radius (Miles)</p>
          <input type="text" value={travelRadius} onChange={(e) => setTravelRadius(e.target.value)}/>
        </div>

        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
}
