import { useState, useEffect } from 'react';
import "./RoundDetail.css"


export default function RoundDetail({roundId, onClose}) {
    const [ roundData, setRoundData ] = useState(null)
    const [ loading, setLoading ] = useState(true)
  

    useEffect(() => {
        const fetchData = async () => {
                try {
                    const roundResponse = await fetch(`http://localhost:8000/round/${roundId}`);
                    const roundData = await roundResponse.json();
                    setRoundData(roundData)
                    setLoading(false)
                } catch (error) {
                    console.error("error fetching data", error)
                    setLoading(false)
                }
            }
            fetchData();
    }, [roundId])
    
    

    if (loading) return <div className="loading">Loading...</div>;

    return(
    <div className='overlay'>
        <div className='score-card-container'>
            <button onClick={onClose}>← Back</button>
            <div className='score-card-data'>
                <p className='hero-meta'>{roundData.course_name} · {roundData.course_location}</p>
                <p className='hero-score'>{roundData.score}</p>
                <p className='hero-meta'>{roundData.tees} · {roundData.holes_played} · {new Date(roundData.date).toLocaleDateString()}</p>
            </div>
            <div className='score-card-analytics'>
                <div>
                    <p className='stat-label'>VS PAR</p>
                    <p className='stat-value'>{roundData.vs_par > 0 ? `+${roundData.vs_par}` : roundData.vs_par}</p>
                </div>
                <div>
                    <p className='stat-label'>HANDICAP</p>
                    <p className='stat-value'>{roundData.handicap}</p>
                </div>
                <div>
                    <p className='stat-label'>NET RATING</p>
                    <p className='stat-value'>{roundData.net_rating}</p>
                </div>
            </div>
            <div className='score-card-course'>
                <div>
                    <p className='course-label'>Rating</p>
                    <p className='course-value'>{roundData.course_rating}</p>
                </div>
                <div>
                    <p className='course-label'>Slope</p>
                    <p className='course-value'>{roundData.course_slope}</p>
                </div>
                <div>
                    <p className='course-label'>Par</p>
                    <p className='course-value'>{roundData.course_par}</p>
                </div>
                <div>
                    <p className='course-label'>Length</p>
                    <p className='course-value'>{roundData.course_length}</p>
                </div>
            </div>
        </div>
    </div>
)
}