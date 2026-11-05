# ⏰ Digital Clock – Digital Logic Design Project

## 📌 Project Overview
This project is a Digital Clock developed as part of the Digital Logic Design (DLD) course.

The project demonstrates digital logic concepts through the design and implementation of MOD counters, logical functions, circuit simulation, and hardware integration.

## 🎯 Project Objectives
- Design MOD-6, MOD-10, and MOD-24 counters.
- Develop truth tables and Karnaugh maps (K-maps).
- Derive and implement logical functions.
- Simulate the digital circuit.
- Build a hardware implementation using Arduino and electronic components.

## ⚙️ Project Components

### Hardware Components
- Arduino Uno R3
- DS3231 Real-Time Clock (RTC) Module
- 1602A LCD Display
- Breadboard
- Jumper Wires
- TMB12A12 Buzzer
- 220Ω Resistors
- 1kΩ Resistor
- 10kΩ Potentiometer
- On/Off and Reset/Set Time Buttons
- USB Cable

## 🧠 Digital Logic Design

The project uses three main counters:

| Counter | Function |
|---|---|
| MOD-6 | Counts from 0 to 5 |
| MOD-10 | Counts from 0 to 9 |
| MOD-24 | Counts from 0 to 23 |

### Logical Functions

**MOD-6 Counter**
- Q0+ = Q0'
- Q1+ = Q1'
- Q2+ = Q2'
- R = Q2 Q1

**MOD-10 Counter**
- Q0+ = Q0'
- Q1+ = Q1'
- Q2+ = Q2'
- Q3+ = Q3'
- R = Q3 Q1

## 🔌 Circuit Simulation

The circuit was simulated using CircuitVerse.

[View Digital Clock Circuit Simulation](https://circuitverse.org/users/425655/projects/digital-clock-88319095-6164-40a8-9391-d596dd827aeb)

## 🖥️ Hardware Implementation

The hardware implementation uses:
- Arduino Uno R3 as the main controller.
- DS3231 RTC module for accurate timekeeping.
- 1602A LCD for displaying time.
- Buzzer for audio alerts.
- Buttons for controlling the clock.

**Supervised by:** Prof. Khaled Hussien

## 📚 References

- [CircuitVerse – 7-Segment Display](https://circuitverse.org/users/27/projects/7-segment-display-cde87bfb-bb9a-477d-b965-bad26494d725)
- [CircuitVerse – 5-Bit to Decimal Decoder](https://circuitverse.org/users/207002/projects/5-bit-to-decimal-decoder-using-2-7-segment-displays)

---

**Course:** Digital Logic Design (DLD)  
**Project:** Digital Clock
