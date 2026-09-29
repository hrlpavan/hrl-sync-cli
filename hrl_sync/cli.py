#!/usr/bin/env python3
"""
HRL Universal Ecosystem Synchronization Engine
Author: Pavan Kumar Sadashiv (Founder & MD, HRL International Private Limited)
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

SCRATCH_DIR = Path("/Users/pavankumars/.gemini/antigravity/scratch")

PROJECTS = {
    "hrl-brand-seo": {
        "path": SCRATCH_DIR / "hrl-brand-seo",
        "url": "https://hrlpavan.github.io/hrl-international-website-/",
        "branches": ["main"],
        "validate": ["python3", "validate_seo.py"]
    },
    "hrl-lang": {
        "path": SCRATCH_DIR / "hrl-lang",
        "url": "https://hrlpavan.github.io/hrl-lang/",
        "branches": ["main", "gh-pages"],
        "validate": ["python3", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]
    },
    "hrl-project-extreme": {
        "path": SCRATCH_DIR / "hrl-project-extreme",
        "url": "https://hrlpavan.github.io/hrl-project-extreme/",
        "branches": ["main", "gh-pages"],
        "validate": None
    },
    "hrlpavan": {
        "path": SCRATCH_DIR / "hrlpavan",
        "url": "https://github.com/hrlpavan",
        "branches": ["main"],
        "validate": None
    },
    "omnitransform-ai-resources": {
        "path": SCRATCH_DIR / "omnitransform-ai-resources",
        "url": "https://hrlpavan.github.io/omnitransform-ai-resources/?v=header_ux_fixed",
        "branches": ["main"],
        "validate": None
    },
    "hrl-x-noise-cancellation": {
        "path": SCRATCH_DIR / "hrl-x-noise-cancellation",
        "url": "https://hrlpavan.github.io/hrl-x-noise-cancellation/",
        "branches": ["main"],
        "validate": ["python3", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]
    }
}

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=isinstance(cmd, str))
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def rollout(message="feat: synchronized ecosystem rollout"):
    print("=" * 60)
    print("HRL UNIVERSAL ECOSYSTEM ROLLOUT ENGINE")
    print("Founder & MD: Pavan Kumar Sadashiv | HRL International Pvt. Ltd.")
    print("=" * 60)
    
    results = []
    
    for name, config in PROJECTS.items():
        path = config["path"]
        if not path.exists():
            print(f"[-] Skipping {name} (Directory not found)")
            continue
            
        print(f"\n[+] Processing: {name} ({path})")
        
        # Validation
        if config["validate"]:
            print(f"    * Running Validation: {' '.join(config['validate'])}")
            rc, out, err = run_cmd(config["validate"], cwd=path)
            if rc != 0:
                print(f"    [!] Validation Failed for {name}: {err or out}")
            else:
                print(f"    [OK] Validation Passed.")

        # Stage and check diff
        run_cmd("git add .", cwd=path)
        rc, status, _ = run_cmd("git status --porcelain", cwd=path)
        
        if status:
            print(f"    * Committing changes...")
            commit_rc, commit_out, _ = run_cmd(f'git commit -m "{message}"', cwd=path)
            if commit_rc == 0:
                print(f"    [OK] Committed: {message}")
            else:
                print(f"    [!] Commit note: {commit_out}")
        else:
            print(f"    * No new uncommitted changes.")

        # Push to remote branches
        for branch in config["branches"]:
            print(f"    * Pushing to origin/{branch}...")
            if branch == "gh-pages":
                push_rc, push_out, push_err = run_cmd("git push origin main:gh-pages --force", cwd=path)
            else:
                push_rc, push_out, push_err = run_cmd(f"git push origin {branch}", cwd=path)
                
            if push_rc == 0:
                print(f"    [OK] Pushed to {branch}.")
            else:
                print(f"    [!] Push note ({branch}): {push_err or push_out}")

        results.append((name, config["url"], "LIVE"))

    print("\n" + "=" * 60)
    print("ROLLOUT COMPLETE - LIVE ECOSYSTEM DIRECTORY")
    print("=" * 60)
    for name, url, status in results:
        print(f"• {name.ljust(28)} : {url}")
    print("=" * 60 + "\n")

    # Automatically trigger daily-project-updates quick-update
    quick_update_bin = SCRATCH_DIR / "daily-project-updates" / "quick-update"
    if quick_update_bin.exists():
        print("[+] Triggering Daily Project Updates Auto-Sync...")
        subprocess.run([str(quick_update_bin)])

def main():
    parser = argparse.ArgumentParser(description="HRL Universal Project Sync & Rollout Tool")
    parser.add_argument("command", choices=["rollout", "status", "test", "daily"], default="rollout", nargs="?", help="Command to run")
    parser.add_argument("-m", "--message", default="feat: universal ecosystem feature synchronization", help="Commit message")
    args = parser.parse_args()

    if args.command == "rollout":
        rollout(message=args.message)
    elif args.command == "daily":
        quick_update_bin = SCRATCH_DIR / "daily-project-updates" / "quick-update"
        if quick_update_bin.exists():
            subprocess.run([str(quick_update_bin)])
        else:
            print("daily-project-updates quick-update script not found.")
    elif args.command == "status":
        print("Checking ecosystem status...")
        for name, config in PROJECTS.items():
            path = config["path"]
            if path.exists():
                _, status, _ = run_cmd("git status -s", cwd=path)
                print(f"{name}: {'Clean' if not status else 'Modified'}")
    elif args.command == "test":
        print("Running ecosystem validation suites...")
        for name, config in PROJECTS.items():
            if config["validate"] and config["path"].exists():
                print(f"Testing {name}...")
                rc, out, _ = run_cmd(config["validate"], cwd=config["path"])
                print(f"  Result: {'PASS' if rc == 0 else 'FAIL'}")

if __name__ == "__main__":
    main()

