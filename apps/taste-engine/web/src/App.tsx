export default function App() {
  return (
    <main>
      <p className="eyebrow">YOUR HOUSEHOLD GUIDE</p>
      <header>
        <div>
          <h1>Discover</h1>
          <p className="intro">Your next favorite is waiting to be found.</p>
        </div>
        <span className="region">UNITED STATES · 01</span>
      </header>
      <section className="empty-state" aria-label="Discover recommendations">
        <span className="orbit" aria-hidden="true">
          ✳
        </span>
        <h2>A good story starts with you.</h2>
        <p>
          Your recommendations will appear here as your taste takes shape.
          Import a watch history or add a few reactions to get started.
        </p>
      </section>
    </main>
  );
}
