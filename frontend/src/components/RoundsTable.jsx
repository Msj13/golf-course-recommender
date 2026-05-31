import {useState, useEffect} from 'react'


export default function RoundsTable() {

    const [rounds, setRounds] = useState(null);
    const [loading, setLoading] = useState(true);


    useEffect(() => {
        fetch('http://localhost:8000/rounds/user/1')
        .then(response => response.json())
        .then(data => {
            setRounds(data)
            setLoading(false)
        })
    }, [])

    if (loading) return <p>Loading rounds...</p>;

    return(
        <div className="bg-white rounded-lg shadow-lg p-8 overflow-x-auto">
  <h3 className="text-2xl font-bold text-gray-800 mb-6">Recent Rounds</h3>
  <table className="w-full">
    <thead>
      <tr className="border-b-2 border-gray-300">
        <th className="px-4 py-3 text-left text-gray-700 font-bold">Course Name</th>
        <th className="px-4 py-3 text-left text-gray-700 font-bold">Score</th>
        <th className="px-4 py-3 text-left text-gray-700 font-bold">Tees</th>
        <th className="px-4 py-3 text-left text-gray-700 font-bold">Holes</th>
        <th className="px-4 py-3 text-left text-gray-700 font-bold">Date</th>
      </tr>
    </thead>
    <tbody>
      {rounds && rounds.map(round => (
        <tr key={round.id} className="border-b border-gray-200 hover:bg-gray-50">
          <td className="px-4 py-4 text-gray-800">{round.course_name}</td>
          <td className="px-4 py-4 font-bold text-lg">{round.score}</td>
          <td className="px-4 py-4 text-gray-600">{round.tees}</td>
          <td className="px-4 py-4 text-gray-600">{round.holes_played}</td>
          <td className="px-4 py-4 text-gray-600">{new Date(round.date).toLocaleDateString()}</td>
        </tr>
      ))}
    </tbody>
  </table>
</div>
    );


}
