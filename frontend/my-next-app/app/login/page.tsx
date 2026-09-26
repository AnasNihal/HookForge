"use client";

import Link from "next/link";
import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState("");
  const submit = (event: FormEvent<HTMLFormElement>) => { event.preventDefault(); setError(""); router.push("/dashboard"); };
  return <main className="auth-page"><AuthArt title="The signal behind every delivery." text="Keep your team close to the moments that matter. HookForge makes webhook debugging feel less like archaeology." /><section className="auth-form-side"><div className="auth-form-wrap"><Link href="/" className="brand"><span className="brand-mark">H</span><span>HookForge</span></Link><h2>Welcome back</h2><p>Sign in to your workspace to continue.</p><form className="auth-form" onSubmit={submit}><div className="form-field"><label htmlFor="email">Work email</label><input id="email" type="email" placeholder="you@company.com" required /></div><div className="form-field"><div style={{ display: "flex", justifyContent: "space-between" }}><label htmlFor="password">Password</label><a className="text-link" style={{ fontSize: 11 }} href="#">Forgot password?</a></div><input id="password" type="password" placeholder="Enter your password" required /></div>{error && <div className="form-error">{error}</div>}<button className="button button-primary form-submit" type="submit">Sign in <span>→</span></button></form><div className="auth-switch">Don&apos;t have a workspace? <Link href="/register">Create one free</Link></div></div></section></main>;
}

function AuthArt({ title, text }: { title: string; text: string }) { return <section className="auth-art"><Link href="/" className="brand brand-large"><span className="brand-mark">H</span><span>HookForge</span></Link><div className="auth-quote"><span className="eyebrow"><span className="pulse-dot" /> Built for reliable systems</span><h1>{title}</h1><p>{text}</p></div><div className="auth-art-footer">© 2026 HookForge · Webhook observability</div></section>; }
