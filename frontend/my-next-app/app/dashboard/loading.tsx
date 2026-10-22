export default function DashboardLoading() {
  return <main className="dashboard-loading" aria-busy="true" aria-label="Loading dashboard"><div className="loading-bar loading-title" /><div className="loading-grid">{[1, 2, 3, 4].map((item) => <div className="loading-card" key={item}><div className="loading-bar loading-small" /><div className="loading-bar loading-value" /><div className="loading-bar loading-foot" /></div>)}</div><div className="loading-columns"><div className="loading-card loading-chart" /><div className="loading-card loading-activity" /></div></main>;
}
