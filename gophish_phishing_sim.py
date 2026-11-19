import os
import json
from datetime import datetime, timezone

BASE_DIR = os.path.expanduser("~/internee-phishing-awareness")
CFG_FILE = os.path.join(BASE_DIR, "templates/gophish_campaign_config.json")
LOG_FILE = os.path.join(BASE_DIR, "logs/phishing_events.jsonl")

def main():
    with open(CFG_FILE) as f:
        cfg = json.load(f)

    # Simulated authorized training recipients & interaction events
    interactions = [
        {"recipient": "intern_01@example.test", "template_id": "TPL-01", "opened": True, "clicked": False, "submitted": False, "reported": True},
        {"recipient": "intern_02@example.test", "template_id": "TPL-01", "opened": True, "clicked": True, "submitted": False, "reported": False},
        {"recipient": "intern_03@example.test", "template_id": "TPL-02", "opened": True, "clicked": True, "submitted": True, "reported": False},
        {"recipient": "staff_04@example.test", "template_id": "TPL-02", "opened": True, "clicked": False, "submitted": False, "reported": True},
        {"recipient": "intern_05@example.test", "template_id": "TPL-01", "opened": False, "clicked": False, "submitted": False, "reported": False}
    ]

    with open(LOG_FILE, "w") as lf:
        for item in interactions:
            rec = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "campaign": cfg["campaign_name"],
                **item
            }
            lf.write(json.dumps(rec) + "\n")
            outcome = "REPORTED" if item["reported"] else ("SUBMITTED" if item["submitted"] else ("CLICKED" if item["clicked"] else ("OPENED" if item["opened"] else "NO_ACTION")))
            print(f"[GOPISH-SIM] {item['recipient']} ({item['template_id']}) -> {outcome}")

    print(f"[+] Recorded {len(interactions)} simulated GoPhish training interactions.")

if __name__ == "__main__":
    main()
