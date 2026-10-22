"use client";

export default function DashboardError({ reset }: { reset: () => void }) {
  return <main className="dashboard-state"><div className="state-icon state-icon-error">!</div><h1>We couldn&apos;t load this view</h1><p>The mock workspace hit a temporary problem. Try the page again or return to the overview.</p><div className="state-actions"><button className="button button-primary" onClick={reset}>Try again</button><a className="button button-soft" href="/dashboard">Back to overview</a></div></main>;
}
