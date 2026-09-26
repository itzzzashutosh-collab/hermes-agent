#!/usr/bin/env python3
"""
Upgrade the remaining standalone skills to full-length (210-240+ lines):
- b2b-sales-constraint-diagnosis
- offers
- sales-script
- sales-market-sizing
- storybrand-messaging
- marketing-mindset
- whatsapp-marketing
- brand-strategy
- probing
- sales-automator
- relationship-led-link-building

Dual install into workspace and Hermes LocalAppData.
"""

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
    print(f"Upgraded dual skill: {skill_name} ({len(content.strip().splitlines())} lines)")

def write_legend_companion(dept: str, legend_folder: str, filename: str, content: str):
    p1 = WORKSPACE_SWATCH / dept / legend_folder / filename
    p2 = HERMES_SWATCH / dept / legend_folder / filename
    ensure_parent(p1)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    ensure_parent(p2)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Updated companion in {dept}/{legend_folder}: {filename} ({len(content.strip().splitlines())} lines)")

print("Initializing standalone skill upgrades...")
