import os
import shutil
import stat

ROOT = r"d:\Sharma Industries Erp Software"
HERMES = os.path.join(ROOT, "hermes-agent")
HERMES_SKILLS = os.path.join(HERMES, "skills")
HERMES_KNOWLEDGE = os.path.join(HERMES, "knowledge", "swatch_paints")
HERMES_SCRATCH = os.path.join(HERMES, "scratch")

os.makedirs(HERMES_SKILLS, exist_ok=True)
os.makedirs(HERMES_KNOWLEDGE, exist_ok=True)
os.makedirs(HERMES_SCRATCH, exist_ok=True)

def remove_readonly(func, path, excinfo):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass

def safe_copy_tree(src, dst):
    if not os.path.exists(src):
        return
    for root, dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        target_dir = os.path.join(dst, rel) if rel != "." else dst
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            s_file = os.path.join(root, f)
            d_file = os.path.join(target_dir, f)
            if not os.path.exists(d_file):
                try:
                    shutil.copy2(s_file, d_file)
                except Exception as e:
                    pass

print("Consolidating temp skills into hermes-agent/skills...")
temp_skill_dirs = ["temp_batch3_skills", "temp_external_skills", "temp_new_skills"]
for ts_name in temp_skill_dirs:
    ts_path = os.path.join(ROOT, ts_name)
    if os.path.exists(ts_path):
        for s_item in os.listdir(ts_path):
            s_item_path = os.path.join(ts_path, s_item)
            if os.path.isdir(s_item_path):
                dest_path = os.path.join(HERMES_SKILLS, s_item)
                safe_copy_tree(s_item_path, dest_path)
                print(f"Migrated skill {s_item} -> hermes-agent/skills")

items_to_delete = [
    "swatch-paints", "skills", "research", "reports", "production",
    "temp_batch3_skills", "temp_external_skills", "temp_new_skills",
    "temp_nous_repos", "temp_shubham_repo", "nps_churn_metric_calc.py",
    "omniroute_custom_benchmark.json", "OMNIROUTE_MODELS.md",
    "omniroute_top_models.json", "omniroute-tested-models.json",
    "competitor-research", "paint-formulation-and-chemicals"
]

print("\nDeleting redundant root directories and files...")
for item in items_to_delete:
    p = os.path.join(ROOT, item)
    if os.path.exists(p):
        if os.path.isdir(p):
            shutil.rmtree(p, onerror=remove_readonly)
            print(f"Deleted directory: {item}")
        else:
            try:
                os.chmod(p, stat.S_IWRITE)
                os.remove(p)
                print(f"Deleted file: {item}")
            except Exception as e:
                print(f"Error removing file {item}: {e}")

print("\nCleanup successfully completed!")
