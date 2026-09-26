"""
File-Based Planning Protocol (adapted from OthmanAdi/planning-with-files).
Provides persistent disk-backed working memory for multi-step Hermes tasks:
- task_plan.md: Structured checklist with active step tracking
- findings.md: Accumulated verified data facts across turns
- progress.md: Monotonic milestone audit log
Crash-proof across session compaction and /clear commands.
"""

import os
from pathlib import Path
from typing import List, Dict, Any, Optional

PLAN_FILE = "task_plan.md"
FINDINGS_FILE = "findings.md"
PROGRESS_FILE = "progress.md"

class FilePlanner:
    def __init__(self, workspace_dir: str):
        self.workspace = Path(workspace_dir)
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.plan_path = self.workspace / PLAN_FILE
        self.findings_path = self.workspace / FINDINGS_FILE
        self.progress_path = self.workspace / PROGRESS_FILE

    def init_plan(self, task_name: str, steps: List[str]) -> Dict[str, Any]:
        """Initialize or reset task_plan.md with numbered steps."""
        lines = [
            f"# Task Plan: {task_name}",
            "",
            "## Objectives & Milestones",
            ""
        ]
        for idx, step in enumerate(steps, 1):
            status = "[ ]"
            lines.append(f"{status} Step {idx}: {step}")

        lines.extend([
            "",
            "---",
            "**Status Legend:** `[ ]` Pending | `[>]` In Progress | `[x]` Completed"
        ])
        
        self.plan_path.write_text("\n".join(lines), encoding="utf-8")
        self.findings_path.write_text(f"# Research & Verified Findings: {task_name}\n\n", encoding="utf-8")
        self.progress_path.write_text(f"# Execution Progress Log: {task_name}\n\n- Plan initialized with {len(steps)} steps.\n", encoding="utf-8")
        
        return {
            "status": "INITIALIZED",
            "task_name": task_name,
            "total_steps": len(steps),
            "plan_path": str(self.plan_path)
        }

    def update_step(self, step_index: int, status: str, finding: Optional[str] = None) -> Dict[str, Any]:
        """
        Update status of step_index (1-based): 'pending', 'in_progress', 'completed'.
        Optionally append a discovered finding to findings.md.
        """
        if not self.plan_path.exists():
            return {"status": "ERROR", "message": "Plan not initialized"}

        content = self.plan_path.read_text(encoding="utf-8").splitlines()
        updated = False
        target_marker = "[x]" if status == "completed" else ("[>]" if status == "in_progress" else "[ ]")

        import re
        new_lines = []
        step_text = ""
        for line in content:
            m = re.match(r"^\[([ x>])\]\s+Step\s+(\d+)(?::\s*(.*))?$", line.strip())
            if m:
                current_idx = int(m.group(2))
                if current_idx == step_index:
                    step_text = m.group(3) or ""
                    new_lines.append(f"{target_marker} Step {current_idx}: {step_text}")
                    updated = True
                    continue
            new_lines.append(line)

        if updated:
            self.plan_path.write_text("\n".join(new_lines), encoding="utf-8")
            # Log progress
            with open(self.progress_path, "a", encoding="utf-8") as f:
                f.write(f"- Step {step_index} marked '{status}': {step_text}\n")

        # Record finding if provided
        if finding:
            with open(self.findings_path, "a", encoding="utf-8") as f:
                f.write(f"### Finding from Step {step_index}\n{finding}\n\n")

        return {
            "status": "SUCCESS" if updated else "STEP_NOT_FOUND",
            "step_index": step_index,
            "new_status": status,
            "recorded_finding": bool(finding)
        }

    def get_current_state(self) -> Dict[str, Any]:
        """Read active plan state for prompt re-injection."""
        if not self.plan_path.exists():
            return {"active": False}
        return {
            "active": True,
            "plan": self.plan_path.read_text(encoding="utf-8"),
            "progress_summary": self.progress_path.read_text(encoding="utf-8") if self.progress_path.exists() else ""
        }
