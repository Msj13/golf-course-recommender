import {useState, useEffect} from 'react'
import RoundDetail from './RoundDetail';
import "./RoundsTable.css"


export default function RoundsTable({userId}) {

    const [rounds, setRounds] = useState(null);
    const [loading, setLoading] = useState(true);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [selectedRound, setSelectedRound] = useState(null);


    useEffect(() => {
        fetch(`http://localhost:8000/rounds/user/${userId}`)
        .then(response => response.json())
        .then(data => {
            setRounds(data)
            setLoading(false)
        })
    }, [userId])

    if (loading) return <p>Loading rounds...</p>;
    if (!rounds || rounds.length === 0) return <p>No rounds found</p>;

    const currentRound = rounds[currentIndex];
    const nextRound = rounds[currentIndex + 1];

    const handleNext = () => {
      if (currentIndex < rounds.length - 1) {
        setCurrentIndex(currentIndex + 1);
      }
    };

    const handlePrev = () => {
      if (currentIndex > 0) {
        setCurrentIndex(currentIndex - 1);
      }
    };

    return(
        <div>
          <h3>Recent Rounds ({currentIndex + 1} of {rounds.length})</h3>
          <div className="cards-display">
            
            {/* Main Card */}
            <div className="main-card">
              <div className="round-card" onClick={() => setSelectedRound(currentRound)}>
                <div>
                  <p>Course</p>
                  <p>{currentRound.course_name}</p>
                </div>
                <div>
                  <p>Score</p>
                  <p>{currentRound.score}</p>
                </div>
                <div>
                  <p>Tees</p>
                  <p>{currentRound.tees}</p>
                </div>
                <div>
                  <p>Holes</p>
                  <p>{currentRound.holes_played}</p>
                </div>
                <div>
                  <p>Date</p>
                  <p>{new Date(currentRound.date).toLocaleDateString()}</p>
                </div>
              </div>
            </div>

            {/* Preview of Next Card */}
            {nextRound && (
              <div className="preview-card">
                <p className="preview-label">Next</p>
                <div className="round-card preview">
                  <div>
                    <p>Course</p>
                    <p>{nextRound.course_name}</p>
                  </div>
                  <div>
                    <p>Score</p>
                    <p>{nextRound.score}</p>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Navigation Buttons */}
          <div className="nav-buttons">
            <button onClick={handlePrev} disabled={currentIndex === 0}>← Previous</button>
            <button onClick={handleNext} disabled={currentIndex === rounds.length - 1}>Next →</button>
          </div>

          {/* Round Detail Card */}
          {selectedRound && (
            <RoundDetail
              roundId={selectedRound.id}
              onClose={() => setSelectedRound(null)}
            />
          )}
        </div>
    );
}