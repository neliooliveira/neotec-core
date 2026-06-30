export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-dark to-surface">
      <div className="text-center">
        <h1 className="text-5xl font-bold mb-4">NEOTEC Core</h1>
        <p className="text-xl text-gray-400 mb-8">Enterprise Management Platform</p>
        <div className="space-y-4">
          <a href="/dashboard" className="inline-block px-8 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold">
            Dashboard
          </a>
          <a href="/login" className="inline-block px-8 py-3 bg-gray-700 hover:bg-gray-600 rounded-lg font-semibold ml-4">
            Login
          </a>
        </div>
      </div>
    </main>
  )
}
