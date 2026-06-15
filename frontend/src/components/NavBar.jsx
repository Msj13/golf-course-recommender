import { useEffect, useState } from 'react';
import {CircleDot, LayoutDashboard,Flag, Sparkles, BarChart2} from 'lucide-react'
import "./NavBar.css"
import {Link, NavLink, useLocation} from "react-router-dom"

export default function NavBar () {

    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const location = useLocation();

    useEffect(() => {
        const fetchData = async () => {
          try {
            const userResponse = await fetch('http://localhost:8000/users/1');
            const userData = await userResponse.json();
            setUser(userData);
            
            setLoading(false);
    
        
          } catch (error) {
            console.error('Error fetching data:', error);
            setLoading(false);
          }
        };
      
        fetchData();
      }, []);




    if (loading) return <div className="loading">Loading...</div>;
    return(
        <div className="nav-container">
            <Link to="/" className="home-btn">
                <div className="home-icon">
                    <CircleDot/>
                </div>
                <h1 className="nav-title">
                    <span style={{ color: 'var(--color-primary)' }}>Golf</span>
                    <span style={{ color: 'var(--color-text)' }}>Finder</span>
                </h1>
            </Link>
            
            <NavLink to='/dashboard' className={({ isActive }) => `nav-link${isActive || location.pathname === '/' ? ' active' : ''}`}>
                 <LayoutDashboard size={18}/>
                 <p>Dashboard</p>
            </NavLink>
           <NavLink to='/courses' className='nav-link'>
                <Flag size={18}/>
                <p>Courses</p>
           </NavLink>

            <NavLink to='/rounds' className='nav-link'>
                <Sparkles size={18}/>
                <p>Recommendations</p>
            </NavLink>

            <NavLink to='/stats' className='nav-link'>
                <BarChart2 size={18}/>
                <p>Analytics</p>
            </NavLink>


            <NavLink to="/profile" style={ {textDecoration: 'none'} } className='nav-link'>
                <p>{user.name}</p>
                <div className="avatar">
                    <p>{user.name.split(" ").map(word => word[0]).join("").slice(0, 2)}</p>
                </div>
            </NavLink>

        </div>
    )
}

