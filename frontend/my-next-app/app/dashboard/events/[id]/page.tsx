import DashboardClient from "../../dashboard-client";
export default async function EventPage({ params }: { params: Promise<{ id: string }> }) { const { id } = await params; return <DashboardClient section="detail" eventId={id} />; }
