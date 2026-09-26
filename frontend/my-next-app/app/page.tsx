import Link from "next/link";

const features = [
  { icon: "◉", title: "Capture every event", text: "A searchable timeline for every webhook received, delivered, or retried." },
  { icon: "↗", title: "Trace delivery", text: "See every attempt, response, and latency detail in one clean timeline." },
  { icon: "✦", title: "Investigate with AI", text: "Turn noisy failures into a clear explanation and a next best action." },
];

export default function Home() {
  return (
    <main className="marketing-page">
      <nav className="marketing-nav shell-width">
        <Link href="/" className="brand brand-large"><span className="brand-mark">H</span><span>HookForge</span></Link>
        <div className="marketing-links"><a href="#features">Features</a><a href="#workflow">How it works</a><a href="#pricing">Pricing</a></div>
        <div className="nav-actions"><Link href="/login" className="button button-ghost">Log in</Link><Link href="/register" className="button button-primary button-small">Start for free <span>→</span></Link></div>
      </nav>

      <section className="hero shell-width">
        <div className="hero-copy">
          <div className="eyebrow"><span className="pulse-dot" /> Webhook observability for teams</div>
          <h1>Know what your webhooks are doing.</h1>
          <p className="hero-subtitle">HookForge gives your team a calm, complete view of webhook traffic — from the first event to the final delivery attempt.</p>
          <div className="hero-actions"><Link href="/dashboard" className="button button-primary button-large">Open the dashboard <span>→</span></Link><Link href="/register" className="text-link">Create a workspace <span>↗</span></Link></div>
          <div className="hero-trust"><span className="avatar-stack"><i>AS</i><i>MK</i><i>+</i></span> Trusted by teams shipping the next thing</div>
        </div>
        <div className="hero-visual" aria-label="HookForge dashboard preview">
          <div className="glow glow-one" /><div className="glow glow-two" />
          <div className="preview-window">
            <div className="preview-topbar"><span className="window-dots"><i /><i /><i /></span><span className="preview-url">app.hookforge.dev / dashboard</span><span className="preview-avatar">AH</span></div>
            <div className="preview-body">
              <aside className="preview-sidebar"><div className="preview-logo"><span className="brand-mark">H</span> HookForge</div><span className="preview-label">Workspace</span><b>Overview</b><span>Projects</span><span>Endpoints</span><span>Events</span><span>AI investigation</span><div className="preview-sidebar-bottom">⌘ K <small>Quick search</small></div></aside>
              <div className="preview-content"><div className="preview-heading"><div><small>Tuesday, February 12, 2026</small><h3>Good afternoon, Amna <span>✦</span></h3></div><span className="preview-button">Last 24 hours⌄</span></div><div className="preview-stats"><div><small>Events received</small><strong>24,892</strong><em>↗ 12.8%</em></div><div><small>Delivery rate</small><strong>98.7%</strong><em>↗ 2.1%</em></div><div><small>Avg. latency</small><strong>184ms</strong><em className="muted">— 0.4%</em></div></div><div className="preview-chart"><div className="chart-header"><span>Event volume</span><small>Last 24 hours</small></div><div className="fake-chart"><span className="chart-fill" /><span className="chart-line" /></div><div className="chart-axis"><span>12am</span><span>6am</span><span>12pm</span><span>6pm</span><span>Now</span></div></div><div className="preview-events"><div className="chart-header"><span>Recent events</span><small>View all →</small></div>{["payment.succeeded", "order.created", "invoice.paid"].map((event, index) => <div className="preview-event" key={event}><span className={`event-icon event-icon-${index}`}>{index === 0 ? "↗" : index === 1 ? "◈" : "◌"}</span><span>{event}<small>evt_01H{index + 2}8K…</small></span><b className="status-chip status-delivered">Delivered</b><time>{index + 2}m ago</time></div>)}</div></div>
            </div>
          </div>
        </div>
      </section>

      <section id="features" className="feature-section shell-width"><div className="section-intro"><span className="eyebrow">Everything in one place</span><h2>Stop guessing. Start knowing.</h2><p>Built for the moments when “it should have worked” is not a useful answer.</p></div><div className="feature-grid">{features.map((feature) => <article className="feature-card" key={feature.title}><span className="feature-icon">{feature.icon}</span><h3>{feature.title}</h3><p>{feature.text}</p><span className="feature-arrow">→</span></article>)}</div></section>
      <section id="workflow" className="workflow-section shell-width"><div className="workflow-card"><div><span className="eyebrow">A better debugging loop</span><h2>From “what happened?” to “fixed.”</h2><p>HookForge connects the event payload, delivery attempts, response history, and investigation context so your team can move quickly.</p></div><div className="workflow-steps"><div><b>01</b><span>Receive</span><small>Capture the raw event</small></div><div><b>02</b><span>Understand</span><small>Inspect payload & context</small></div><div><b>03</b><span>Resolve</span><small>Replay with confidence</small></div></div></div></section>
      <footer className="marketing-footer shell-width"><Link href="/" className="brand"><span className="brand-mark">H</span><span>HookForge</span></Link><span>© 2026 HookForge. Built for reliable systems.</span><div><Link href="/login">Sign in</Link><Link href="/register">Create workspace</Link></div></footer>
    </main>
  );
}
