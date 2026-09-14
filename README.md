

# AI KiCad Automation 🚀

An AI-powered PCB automation assistant built using **Model Context Protocol (MCP)**.

This project is a learning and portfolio prototype that demonstrates how Artificial Intelligence can communicate with external engineering tools through MCP.

The goal is to create an AI PCB Engineer that can understand natural language instructions and automatically perform PCB design tasks in KiCad.

Example:

```
User:
"Create a PCB project"

AI:
→ Understand request
→ Call MCP tool
→ Generate KiCad project
→ Create PCB file
```

---

# 🌟 Project Overview

Traditional PCB design requires engineers to manually:

* Open KiCad
* Create projects
* Select components
* Place footprints
* Configure board settings
* Modify files

This project explores a future workflow:

```
Human Instruction
        |
        ↓
       AI Assistant
        |
        ↓
   MCP Communication
        |
        ↓
  KiCad Automation Tools
        |
        ↓
  Generated PCB Files
```

The AI does not directly control KiCad.

Instead, it uses **MCP tools** as a safe communication layer between the AI system and engineering software.

---

# 🏗️ System Architecture

```
                 User

                  |
                  ↓

             React Web UI

                  |
                  ↓

          FastAPI Bridge Server

                  |
                  ↓

             MCP Client

                  |
                  ↓

        Model Context Protocol

                  |
                  ↓

          Custom KiCad MCP Server

                  |
                  ↓

          KiCad File Generator

                  |
                  ↓

          .kicad_pcb File
```

---

# 🔥 What is MCP?

**Model Context Protocol (MCP)** is a communication standard that allows AI models to interact with external tools and applications.

Think of MCP like a universal connector.

Example:

Without MCP:

```
AI
 |
 X
 |
KiCad
```

AI cannot safely access KiCad.

With MCP:

```
AI
 |
 MCP
 |
Tool
 |
KiCad
```

The AI can request actions through defined tools.

---

# ✨ Current Features (Version 1.0)

## ✅ Custom MCP Server

A dedicated MCP server created for KiCad automation.

Location:

```
backend/kicad_mcp_server/
```

---

## ✅ MCP Tools

Currently available tools:

### 1. Create KiCad Project

Tool:

```
create_kicad_project()
```

Example:

```json
{
 "project_name":"demo_board"
}
```

Creates:

```
demo_board.kicad_pcb
```

---

### 2. Place Header Component

Tool:

```
place_header()
```

Example:

```json
{
 "pins":4,
 "x_mm":80,
 "y_mm":45,
 "rotation":90
}
```

This represents a PCB component placement instruction.

---

# 🛠️ Technologies Used

## Backend

* Python
* FastAPI
* Model Context Protocol (MCP)
* Pydantic

## Frontend

* React
* Vite
* JavaScript

## PCB Automation

* KiCad PCB format
* Custom PCB generator

---

# 📂 Project Structure

```
ai-kicad-copilot/

│
├── frontend/
│   └── React Web Interface
│
├── backend/
│
│   ├── bridge/
│   │   ├── FastAPI server
│   │   └── MCP client
│
│   ├── kicad_mcp_server/
│   │   ├── MCP server
│   │   ├── Tool definitions
│   │   └── PCB generator
│
│   └── kicad/
│       └── Generated files
│
└── tests/
```

---

# 🚀 How It Works

Example workflow:

### Step 1

User enters:

```
Create a PCB project
```

---

### Step 2

React sends request:

```
Browser
 ↓
FastAPI API
```

---

### Step 3

FastAPI calls MCP Client:

```
MCP Client
 ↓
create_kicad_project()
```

---

### Step 4

MCP Server executes tool:

```
KiCad MCP Server
 ↓
PCB Generator
```

---

### Step 5

Output:

```
demo_board.kicad_pcb
```

is generated.

---

# 🧑‍💻 Beginner Setup

## Requirements

Install:

* Python 3.10+
* Node.js
* KiCad
* Git

---

## Backend Setup

Go to:

```
backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn bridge.main:app --port 8787
```

---

## Frontend Setup

Go to:

```
frontend
```

Install dependencies:

```bash
npm install
```

Start:

```bash
npm run dev
```

Open:

```
http://localhost:5173
```

---

# 🧪 Testing MCP Server

Run:

```bash
python test_client.py
```

Expected:

```
before init
after init

Available tools:

- create_kicad_project
- place_header
```

---

# 🗺️ Roadmap

## Version 1.1

Real PCB component generation:

* Real KiCad footprints
* Component placement
* Modify existing PCB files

## Version 1.2

AI Understanding Layer:

* Natural language PCB commands
* Prompt parsing
* AI planning

## Version 2.0

Advanced PCB Engineer:

* Automatic routing
* Design rule checking
* Component suggestions
* Complete PCB generation

---

# 🎯 Project Goal

This project is an exploration of how AI agents can become engineering assistants.

The long-term vision:

```
Engineer:
"Design a sensor board with ESP32 and temperature sensor"

AI:
→ Select components
→ Create schematic
→ Place footprints
→ Route PCB
→ Generate KiCad files
```

---


