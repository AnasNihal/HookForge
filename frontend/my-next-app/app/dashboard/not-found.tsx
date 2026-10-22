import Link from "next/link";

export default function DashboardNotFound() {
  return <main className="dashboard-state"><div className="state-icon">⌕</div><h1>That dashboard view isn&apos;t here</h1><p>The page may have moved, or the link may be from a different workspace.</p><Link className="button button-primary" href="/dashboard">Return to overview</Link></main>;
}
