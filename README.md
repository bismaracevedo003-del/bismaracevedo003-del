# Bismarck Acevedo

[![Links](https://github.com/bismaracevedo003-del/bismaracevedo003-del/actions/workflows/link-check.yml/badge.svg)](https://github.com/bismaracevedo003-del/bismaracevedo003-del/actions/workflows/link-check.yml)
![Electronic Engineer](https://img.shields.io/badge/Electronic_Engineer-Automation-blue)
![PLC/SCADA](https://img.shields.io/badge/PLC%2FSCADA-Industrial_Control-green)
![Portfolio](https://img.shields.io/badge/Portfolio-7_projects-orange)

**Electronic Engineer · Industrial Automation · PLC/SCADA · Instrumentation**

I build reproducible control-system prototypes with runnable simulations, explicit evidence boundaries and production-style documentation. Across the portfolio: **7 public projects** and **180 automated checks verified locally**.

---

## Profile

I work on industrial control sequencing, SCADA/HMI design, instrumentation models and the software bridges that connect them. The repositories below are complete engineering artifacts: source, documentation, diagrams, tests and visual evidence. When a feature is simulated rather than running on real hardware, the repository says so clearly.

> **Nota (ES):** Ingeniero electrónico enfocado en automatización industrial. Publico proyectos con código, documentación técnica, pruebas y simulación reproducible; cuando no hay hardware real, lo indico explícitamente.

## Engineering focus

- **Control:** Siemens S7-1200, TIA Portal V19, Ladder/SCL, Allen-Bradley Micro850, CCW.
- **Protocols:** Modbus TCP, S7-style tag models, REST/WebSocket bridges and MQTT-style telemetry.
- **Instrumentation:** 4–20 mA loops, FOPDT process models, PID tuning, anti-windup and fault injection.
- **Software:** Python process models, Node.js/Express, React/Vite, MySQL, SQLite, Docker and Git.
- **Evidence:** unit tests, API smoke checks, SVG screenshots and optional real-mode adapters.

## Repository map

| Project | Scope | Verified checks | Stack |
| --- | --- | --- | --- |
| [scada-water-pumping](https://github.com/bismaracevedo003-del/scada-water-pumping) | Dual-pump water station, REST/WebSocket bridge and React SCADA dashboard | 11 Node + 20 Python | S7-1200, Node.js, React, MySQL |
| [plc-motor-control-vfd](https://github.com/bismaracevedo003-del/plc-motor-control-vfd) | 4–20 mA VFD control with ramps, interlocks and fault latching | 25 Python | S7-1200, SCL/Ladder, Python |
| [micro850-conveyor-automation](https://github.com/bismaracevedo003-del/micro850-conveyor-automation) | Sorting conveyor with photoeyes, diverter, jam detection and Modbus TCP | 26 Python | Micro850, Ladder, Python |
| [industrial-instrumentation-simulator](https://github.com/bismaracevedo003-del/industrial-instrumentation-simulator) | Transmitter faults, FOPDT models, PID anti-windup and live tuning comparison | 33 Python | Python, PID, Canvas HMI |
| [industrial-maintenance-cmms](https://github.com/bismaracevedo003-del/industrial-maintenance-cmms) | Work orders, preventive maintenance, spare parts, downtime and OEE | 23 Python | Python, SQLite, REST API |
| [electro-pneumatic-press](https://github.com/bismaracevedo003-del/electro-pneumatic-press) | Two-hand control, safety relay feedback, anti-tie-down and pneumatic sequence | 20 Python | S7-1200, SCL, Python |
| [iot-energy-monitoring](https://github.com/bismaracevedo003-del/iot-energy-monitoring) | MQTT-style telemetry, tariff analysis, anomaly detection and cost/CO₂ KPIs | 22 Python | Python, MQTT, Canvas HMI |

## How the repositories are structured

- `docs/` — engineering notes, integration guides and decision records.
- `simulation/` — runnable process or device models with deterministic behavior.
- `tests/` — unit and smoke checks for the control logic and APIs.
- `screenshots/` — SVG evidence of the dashboards and fault states.
- `config/real.env.example` — optional real-mode configuration template.

## Verification boundary

- **Default mode:** simulation. Every project runs without external hardware or credentials.
- **Optional real mode:** adapters are prepared for PLC, Modbus, MQTT and MySQL, but they are not validated against physical equipment.
- **Safety scope:** the electro-pneumatic press adapter is read-only; no actuator download or safety validation is claimed.
- **Test evidence:** 180 checks were executed locally across the seven projects.

## Currently building

- More protocol bridges and realistic HMI/SCADA patterns.
- CI and link validation across the portfolio repositories.
- Clearer deployment notes for optional real-mode adapters.

## Contact

Open to industrial automation, PLC programming, SCADA integration and control-software roles. Reach me through [GitHub](https://github.com/bismaracevedo003-del).

---

This repository is named exactly like the GitHub username so this `README.md` is rendered on the profile page.
