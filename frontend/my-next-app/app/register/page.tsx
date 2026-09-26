"use client";

import Link from "next/link";
import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";

export default function RegisterPage() {
  const router = useRouter(); const [error, setError] = useState("");
  const submit = (event: FormEvent<HTMLFormElement>) => { event.preventDefault(); setError(""); router.push("/dashboard"); };
  return <main className="auth-page"><section className="auth-art"><Link href="/" className="brand brand-large"><span className="brand-mark">H</span><span>HookForge</span></Link><div className="auth-quote"><span className="eyebrow"><span className="pulse-dot" /> Your next debugging session</span><h1>Make reliability part of the workflow.</h1><p>Start with a workspace, connect an endpoint, and see your first event in minutes.</p></div><div className="auth-art-footer">© 2026 HookForge · Webhook observability</div></section><section className="auth-form-side"><div className="auth-form-wrap"><Link href="/" className="brand"><span className="brand-mark">H</span><span>HookForge</span></Link><h2>Create your workspace</h2><p>Everything you need to make webhooks observable.</p><form className="auth-form" onSubmit={submit}><div className="form-field"><label htmlFor="name">Your name</label><input id="name" placeholder="Amna Anas" required /></div><div className="form-field"><label htmlFor="register-email">Work email</label><input id="register-email" type="email" placeholder="you@company.com" required /></div><div className="form-field"><label htmlFor="register-password">Create a password</label><input id="register-password" type="password" minLength={8} placeholder="At least 8 characters" required /></div><label className="form-checkbox"><input type="checkbox" required /> <span>I agree to the <a className="text-link" href="#">Terms of Service</a> and <a className="text-link" href="#">Privacy Policy</a>.</span></label>{error && <div className="form-error">{error}</div>}<button className="button button-primary form-submit" type="submit">Create workspace <span>→</span></button></form><div className="auth-switch">Already have an account? <Link href="/login">Sign in</Link></div></div></section></main>;
}
