"use client";

type SettingsViewProps = {
  onNotify: (message: string) => void;
};

export default function SettingsView({ onNotify }: SettingsViewProps) {
  return (
    <>
      <div className="settings-heading">
        <div><h1>Settings</h1><p>Shape how your workspace behaves and how your team hears about failures.</p></div>
        <span className="settings-saved">● All changes are local</span>
      </div>
      <div className="settings-layout">
        <aside className="panel settings-nav" aria-label="Settings sections">
          <button className="settings-nav-item active">Workspace</button>
          <button className="settings-nav-item">Notifications</button>
          <button className="settings-nav-item">Members & access</button>
          <button className="settings-nav-item">API keys</button>
        </aside>
        <div className="settings-sections">
          <section className="panel settings-card">
            <div className="settings-card-heading"><div><h2>Workspace profile</h2><p>Keep the workspace details your team sees across HookForge.</p></div><span className="settings-icon">⌂</span></div>
            <div className="settings-form-grid">
              <div className="form-field"><label htmlFor="workspace-name">Workspace name</label><input id="workspace-name" defaultValue="Acme workspace" /></div>
              <div className="form-field"><label htmlFor="workspace-slug">Workspace slug</label><input id="workspace-slug" defaultValue="acme" /></div>
              <div className="form-field settings-full-field"><label htmlFor="workspace-description">Description</label><textarea id="workspace-description" defaultValue="Reliable delivery monitoring for the Acme team." /></div>
            </div>
            <div className="settings-actions"><button className="button button-primary" onClick={() => onNotify("Workspace profile saved")}>Save changes</button></div>
          </section>
          <section className="panel settings-card">
            <div className="settings-card-heading"><div><h2>Notifications</h2><p>Choose which signals should reach your inbox.</p></div><span className="settings-icon">♧</span></div>
            <div className="settings-toggle-list">
              <Toggle label="Email notifications" detail="Receive important workspace activity by email." />
              <Toggle label="Delivery failures" detail="Alert me when an endpoint returns an error." />
            </div>
            <div className="settings-digest-row"><div><strong>Digest frequency</strong><small>Bundle lower-priority activity into a summary.</small></div><select defaultValue="Daily summary"><option>Daily summary</option><option>Weekly summary</option><option>Never</option></select></div>
            <div className="settings-actions"><button className="button button-primary" onClick={() => onNotify("Notification preferences saved")}>Save preferences</button></div>
          </section>
          <section className="panel settings-card danger-zone"><div className="settings-card-heading"><div><h2>Danger zone</h2><p>Destructive workspace actions are disabled in this mock environment.</p></div><span className="settings-icon danger-icon">!</span></div><button className="button button-danger" onClick={() => onNotify("Workspace deletion is disabled in the demo")}>Delete workspace</button></section>
        </div>
      </div>
    </>
  );
}

function Toggle({ label, detail }: { label: string; detail: string }) {
  return <label className="settings-toggle"><span><strong>{label}</strong><small>{detail}</small></span><input type="checkbox" defaultChecked /><span className="toggle-track" aria-hidden="true"><span /></span></label>;
}
