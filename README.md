# HookForge

A full-stack application built with **Next.js** and **FastAPI**. HookForge is a learning and development project focused on building modern web applications with a separate frontend and backend architecture.

> **Project status:** Under development 🚧

## 📁 Project Structure

```text
HookForge/
├── backend/
│   ├── main.py
│   ├── venv/
│   └── ...
│
├── frontend/
│   └── my-next-app/
│       ├── public/
│       ├── src/
│       ├── package.json
│       └── ...
│
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

### Frontend

* Next.js
* React
* TypeScript / JavaScript
* CSS / Tailwind CSS (if configured)

### Backend

* Python
* FastAPI
* Uvicorn
* Python Virtual Environment

### Development Tools

* Git & GitHub
* Visual Studio Code
* npm / pnpm
* REST API

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure you have the following installed:

* [Git](https://git-scm.com/)
* [Python](https://www.python.org/)
* [Node.js](https://nodejs.org/)
* npm or pnpm
* Visual Studio Code (recommended)

---

## ⚙️ Backend Setup

The backend is built using FastAPI.

### 1. Navigate to the backend

From the project root:

```bash
cd backend
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install "fastapi[standard]"
```

### 5. Run the backend server

```bash
fastapi dev main.py
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### API Documentation

FastAPI provides interactive API documentation:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 💻 Frontend Setup

The frontend is built using Next.js.

### 1. Open a new terminal

Keep the backend running and open another terminal window.

### 2. Navigate to the frontend

From the project root:

```bash
cd frontend/my-next-app
```

### 3. Install dependencies

If the project uses npm:

```bash
npm install
```

If the project uses pnpm:

```bash
pnpm install
```

Use the package manager that matches your project's lockfile.

### 4. Start the development server

For npm:

```bash
npm run dev
```

For pnpm:

```bash
pnpm dev
```

The frontend will usually run at:

```text
http://localhost:3000
```

---

## 🔗 Application Architecture

The project uses a separate frontend and backend architecture.

```text
User
  │
  ▼
Next.js Frontend
  │
  │ HTTP Requests
  ▼
FastAPI Backend
  │
  ▼
Application Logic
  │
  ▼
Database / External Services
```

The frontend handles the user interface, while the backend manages API endpoints and application logic.

## 🔧 Development Workflow

1. Create or update a backend API endpoint using FastAPI.
2. Test the endpoint using FastAPI's interactive documentation.
3. Build the frontend interface using Next.js.
4. Connect the frontend to the backend API.
5. Test the complete application.
6. Commit changes using Git.

## 🧪 Testing the Backend

The backend root endpoint can be tested using:

```bash
curl http://127.0.0.1:8000/
```

You can also open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔐 Environment Variables

If the project uses environment variables, create a `.env` file in the appropriate project directory.

Example:

```env
API_URL=http://127.0.0.1:8000
```

**Do not commit sensitive information such as API keys, passwords, or private tokens.**

## 🌱 Git Workflow

From the HookForge root directory:

```bash
git status
git add .
git commit -m "Describe your changes"
git push origin main
```

Keep the main Git repository at the project root:

```text
HookForge/
```

## 🗺️ Roadmap

* [x] Set up the project repository
* [x] Create the FastAPI backend
* [x] Set up the Next.js frontend
* [ ] Build core application features
* [ ] Connect frontend and backend
* [ ] Add database integration
* [ ] Add testing
* [ ] Deploy the application

## 📌 Project Status

HookForge is actively being developed. Features, architecture, and technologies may change as the project evolves.

## 👨‍💻 Author

**Anas Nihal**

* GitHub: [AnasNihal](https://github.com/AnasNihal)

---

Built with Python, FastAPI, Next.js, and a continuous learning mindset. 🚀
