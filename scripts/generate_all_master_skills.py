#!/usr/bin/env python3
"""
Generate comprehensive, full-length (230-350+ line) master skills:
1. building-rapport (Louis Blythe + Joe Girard)
2. company-brain (Corey Haines MakerSkills + Swatch Enterprise OS)
3. straight-line-closer (Daniel Gap + Jordan Belfort + Oyi77)
4. revenue-data-governance-strategy (Maya-Beth Finotti RevOps)
5. finance-expert (Persona Management Layer + Kaplan + Buffett)
6. elon-musk-perspective (xmg2024 First-Principles Manufacturing)
7. product-strategy (899ms + Phuryn + Michael Porter)
8. persona-hr-coordinator (Google Workspace + Geoff Smart)
9. industry-use-case-builder (Adobe Blueprints + B2B Coatings)

Dual installs into:
- hermes-agent/skills/<name>/SKILL.md
- C:\\Users\\itzzz\\AppData\\Local\\hermes\\skills\\<name>\\SKILL.md
And into respective Swatch Paints legend companion folders.
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
