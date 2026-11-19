import os
import json

BASE_DIR = os.path.expanduser("~/internee-phishing-awareness")
LOG_FILE = os.path.join(BASE_DIR, "logs/phishing_events.jsonl")
REPORT_MD = os.path.join(BASE_DIR, "AWARENESS_REPORT.md")
SUMMARY_OUT = os.path.join(BASE_DIR, "submission_summary.txt")

def main():
    events = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            events = [json.loads(line) for line in f if line.strip()]

    total = len(events)
    opened = sum(1 for e in events if e.get("opened"))
    clicked = sum(1 for e in events if e.get("clicked"))
    submitted = sum(1 for e in events if e.get("submitted"))
    reported = sum(1 for e in events if e.get("reported"))

    click_rate = round((clicked / total) * 100, 1) if total else 0.0
    report_rate = round((reported / total) * 100, 1) if total else 0.0

    summary = "\n".join([
        "Internee.pk Phishing Awareness & GoPhish Simulation Task - Summary",
        f"Total Simulated Recipients: {total}",
        f"Opened: {opened} | Clicked: {clicked} ({click_rate}%) | Submitted Credentials: {submitted} | Reported: {reported} ({report_rate}%)",
        "Training Recommendations: Enforce phishing red-flag micro-training for clicked/submitted users, promote one-click phishing reporting, and require MFA/passkeys on portals."
    ]) + "\n"

    md_lines = [
        "# Internee.pk Security Awareness & Phishing Simulation Report",
        "",
        f"- **Total Targets Simulated:** {total}",
        f"- **Emails Opened:** {opened}",
        f"- **Links Clicked:** {clicked} ({click_rate}%)",
        f"- **Data/Credentials Submitted:** {submitted}",
        f"- **Phishing Reported:** {reported} ({report_rate}%)",
        "",
        "## Key Training Actions",
        "1. Spot urgent/reward lures, lookalike URLs, and unexpected login prompts before clicking.",
        "2. Report suspicious emails immediately instead of forwarding or replying.",
        "3. Use MFA/2FA so even a phished password cannot grant account access."
    ]

    with open(SUMMARY_OUT, "w") as out:
        out.write(summary)

    with open(REPORT_MD, "w") as rm:
        rm.write("\n".join(md_lines) + "\n")

    print(summary)
    print(f"[+] Saved report to: {REPORT_MD} and {SUMMARY_OUT}")

if __name__ == "__main__":
    main()
