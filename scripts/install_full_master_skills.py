#!/usr/bin/env python3
"""
Install Full Master Skills for Swatch Paints & Hermes:
Ensures all newly installed skills are deep, comprehensive, production-grade (220-350+ lines),
fully infused with Swatch Paints (Sharma Industries), Ashutosh Sharma Sir, and Hermes (CEO).
"""

import os
from pathlib import Path

WORKSPACE_ROOT = Path(r"d:\Sharma Industries Erp Software\hermes-agent")
WORKSPACE_SWATCH = WORKSPACE_ROOT / "skills" / "swatch-paints"
WORKSPACE_SKILLS = WORKSPACE_ROOT / "skills"

HERMES_ROOT = Path(r"C:\Users\itzzz\AppData\Local\hermes\skills")
HERMES_SWATCH = HERMES_ROOT / "swatch-paints"

def ensure_parent(p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)

def write_dual(skill_name: str, content: str):
    p1 = WORKSPACE_SKILLS / skill_name / "SKILL.md"
    p2 = HERMES_ROOT / skill_name / "SKILL.md"
    
    ensure_parent(p1)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
        
    ensure_parent(p2)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Installed dual skill: {skill_name} ({len(content.strip().splitlines())} lines)")

def write_legend_companion(dept: str, legend_folder: str, filename: str, content: str):
    p1 = WORKSPACE_SWATCH / dept / legend_folder / filename
    p2 = HERMES_SWATCH / dept / legend_folder / filename
    
    ensure_parent(p1)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
        
    ensure_parent(p2)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Placed companion in {dept}/{legend_folder}: {filename} ({len(content.strip().splitlines())} lines)")

print("Ready to generate full master skills...")
