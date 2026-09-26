import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = { title: "HookForge — Webhook observability", description: "See every webhook. Understand every delivery." };

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
