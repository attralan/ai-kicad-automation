# AI KiCad Automation 🚀

An AI-powered PCB automation assistant built using **Model Context Protocol (MCP)**.

This project demonstrates how Artificial Intelligence can communicate with engineering tools through MCP and automate KiCad design workflows.

The goal is to build an AI PCB Engineer that can understand human instructions and convert them into structured KiCad automation commands.

---

# 🌟 Project Overview

Traditional PCB design requires engineers to manually:

- Create KiCad projects
- Draw schematics
- Select components
- Place footprints
- Configure PCB files

This project explores an AI-assisted workflow:

```
Human Instruction

        ↓

AI Assistant

        ↓

MCP Communication

        ↓

KiCad Automation Tools

        ↓

Generated PCB Files
```

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
        -------------------------

        |                       |

        ↓                       ↓

  KiCad PCB Generator     Schematic Generator

        |                       |

        ↓                       ↓

   .kicad_pcb             .kicad_sch

```

---

# 🔥 What is MCP?

**Model Context Protocol (MCP)** is a communication standard that allows AI systems to interact with external tools.

MCP works as a bridge between AI models and engineering applications.

Without MCP:

```
AI

 |

X

 |

Engineering Tool
```

With MCP:

```
AI

 |

MCP

 |

Tool

 |

Engineering Software
```

---

# ✨ Current Features (Version 1.1)

## ✅ Custom KiCad MCP Server

A dedicated MCP server created for KiCad automation.

Location:

```
backend/kicad_mcp_server/
```

---

# 🛠 MCP Tools

## 1. Create KiCad Project

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

Generates:

```
demo_board.kicad_pcb
```

---

## 2. Create KiCad Schematic

Tool:

```
create_kicad_schematic()
```

Generates:

```
demo_board.kicad_sch
```

---

## 3. Place Header Component

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

Creates a component placement instruction.

---

# 🌐 Web Interface

The project includes a React + Vite frontend.

Features:

✅ Prompt input box

✅ Generate KiCad project button

✅ Backend communication

✅ Generated file display

✅ Download PCB file

✅ Download schematic file

---

# ⚙️ Backend

Built using:

- Python
- FastAPI
- MCP SDK
- Pydantic


API Flow:

```
React

 ↓

FastAPI

 ↓

MCP Client

 ↓

KiCad MCP Server

 ↓

Generated Files
```

---

# 📂 Project Structure

```
ai-kicad-automation/

│
├── frontend/
│
│   ├── src/
│   │
│   ├── App.jsx
│   └── api.js
│
│
├── backend/
│
│   ├── bridge/
│   │
│   │   ├── main.py
│   │   ├── mcp_client.py
│   │   ├── models.py
│   │   └── security.py
│
│
│   ├── kicad_mcp_server/
│   │
│   │   ├── server.py
│   │   ├── tools.py
│   │   ├── pcb_writer.py
│   │   └── kicad_generator.py
│
│
├── README.md
│
└── requirements.txt

```

---

# 🚀 Installation

## Requirements

Install:

- Python 3.10+
- Node.js
- Git
- KiCad


---

# Backend Setup

Go to backend:

```bash
cd backend
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

Run backend:

```bash
uvicorn bridge.main:app --port 8787
```

Backend runs:

```
http://127.0.0.1:8787
```

---

# Frontend Setup

Go to frontend:

```bash
cd frontend
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

Expected output:

```
before init

after init

Available tools:

- create_kicad_project
- create_kicad_schematic
- place_header

```

---

# Example Workflow

User enters:

```
Create a PCB project
```

System performs:

```
React UI

 ↓

FastAPI Request

 ↓

MCP Client

 ↓

create_kicad_project()

 ↓

KiCad Generator

 ↓

demo_board.kicad_pcb

demo_board.kicad_sch

```

---

# 🗺️ Roadmap


# Version 1.2

AI Planning Layer

Features:

- Natural language understanding
- Prompt to MCP tool conversion
- AI decision making


Example:

User:

```
Create a temperature sensor board
```

AI:

```
create_project()

add_ESP32()

add_sensor()

place_components()

generate_files()
```


---

# Version 2.0

Advanced AI PCB Engineer

Planned:

- Real KiCad footprints
- Real schematic components
- Automatic routing
- Design rule checking
- Component recommendation
- Complete PCB generation

---

# 🎯 Project Goal

The long-term vision is an AI engineering assistant.

Example:

Human:

```
Design an ESP32 temperature monitoring board
```

AI:

```
→ Select components

→ Create schematic

→ Place footprints

→ Route PCB

→ Generate KiCad files

```

---

# 📌 Version History


## v1.1

Added:

✅ PCB generation

✅ Schematic generation

✅ MCP tool system

✅ React web interface

✅ FastAPI bridge

✅ File download workflow


## v1.0

Initial prototype:

✅ MCP server

✅ MCP client

✅ Basic KiCad automation


---

# Author

AI KiCad Automation Project

Built as a learning and portfolio project exploring:

- Artificial Intelligence
- Model Context Protocol
- Engineering Automation
- PCB Design Automation
