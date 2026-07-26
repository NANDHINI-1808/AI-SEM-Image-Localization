# AI-Powered Navigation-Error Recovery for Wafer Inspection using SEM Image Localization

## Overview

Semiconductor wafer inspection requires extremely precise positioning to ensure that the inspection tool returns to the exact same location on a wafer repeatedly.

In real manufacturing environments, small navigation errors occur due to thermal expansion, vibration, and mechanical drift. These errors can cause the inspection tool to land on an incorrect location.

This project presents an AI-based SEM image localization approach to recover the correct position by identifying where a reference SEM image pattern appears inside a larger search image.

The system predicts the center coordinates of the matching region and evaluates localization accuracy using multiple test cases.

---

# Problem Statement

Modern wafer inspection tools need nanometer-level positioning accuracy. However, navigation errors can accumulate over repeated inspections.

Due to highly repetitive semiconductor layouts, traditional template matching methods often fail because multiple visually similar regions exist in the wafer image.

The goal of this project is to:

- Locate the reference SEM image pattern inside a search image
- Handle repeated and similar wafer structures
- Estimate the center coordinates of the correct matching region
- Reduce navigation errors during wafer inspection

---

# Proposed Solution

The proposed system uses computer vision-based localization to identify the correct wafer region.

The workflow:
