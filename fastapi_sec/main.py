import argparse
import subprocess


def scan():
    print("🔍 Running security scans...\n")

    # --- Run Bandit ---
    print("▶ Running Bandit (code security)...\n")
    bandit_result = subprocess.run(
        ["bandit", "-r", "."],
        check=False
    )

    # --- Run Safety ---
    print("\n▶ Running Safety (dependency security)...\n")
    safety_result = subprocess.run(
        ["safety", "check"],
        check=False
    )

    # --- Decide overall result ---
    if bandit_result.returncode == 0 and safety_result.returncode == 0:
        print("\n✅ Security check PASSED")
        exit(0)
    else:
        print("\n❌ Security check FAILED")
        exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="FastAPI Security Automation Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("scan", help="Run security checks")

    args = parser.parse_args()

    if args.command == "scan":
        scan()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
