export type EventStatus = "Delivered" | "Failed" | "Retrying" | "Pending";

export type HookEvent = {
  id: string;
  type: string;
  endpoint: string;
  status: EventStatus;
  created: string;
  response: string;
  method: string;
  payload: string;
};

export type Endpoint = {
  name: string;
  path: string;
  method: "GET" | "POST" | "PATCH";
  status: "Active" | "Paused";
  category: string;
  events: string;
  latency: string;
  rate: string;
};

export type TimeRange = "Last 24 hours" | "Last 7 days" | "Last 30 days";

export type ChatMessage = {
  role: "assistant" | "user";
  text: string;
};
