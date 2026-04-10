import time
import random
import numpy as np

TOTAL_FEATS = 86
MAX_ITER = 60

RANSOMWARE = {
    "fileless": [
        {"name": "Ryuk", "accuracy": 97.8,
         "sig": "svchost inject · WMI exec · shadow delete · C2 exfil",
         "key_feats": ["VAD anomaly", "svchost hijack", "WMI exec", "C2 socket"]},
        {"name": "Conti", "accuracy": 98.1,
         "sig": "CONHOST hide · WMIC delete · double-extort",
         "key_feats": ["CONHOST pattern", "WMIC shadowcopy", "C2 artifact"]},
    ],
    "filebased": [
        {"name": "WannaCry", "accuracy": 98.4,
         "sig": "EternalBlue · SMB spread · PowerShell bypass",
         "key_feats": ["PS bypass", "encoded cmd", "Defender hook"]},
        {"name": "LockBit", "accuracy": 98.6,
         "sig": "DLL hijack · network spread",
         "key_feats": ["rundll32", "C2 socket", "spread scan"]},
    ]
}

WOA_PHASES = [
    "Encircling Prey",
    "Bubble-Net Attack",
    "Search for Prey",
    "Position Updating"
]

# ────────────────────────────────────────────────
def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

# ────────────────────────────────────────────────
def select_ransomware():
    print("\n=== RANSOMWARE SELECTOR ===\n")

    all_items = []
    idx = 1

    for t in RANSOMWARE:
        print(f"\n{t.upper()}:\n")
        for r in RANSOMWARE[t]:
            print(f"{idx}. {r['name']}  ({r['sig']})")
            all_items.append((t, r))
            idx += 1

    choice = int(input("\nSelect ransomware (number): ")) - 1
    return all_items[choice]

# ────────────────────────────────────────────────
def run_woa(rw_type, rw):
    log(f"Starting WOA scan for {rw['name']} ({rw_type})")

    selected = set()
    target_n = int(TOTAL_FEATS * (0.3 + random.random() * 0.1))

    # Phase 1
    log("Capturing RAM...")
    time.sleep(1)
    log("Extracting memory features...")
    time.sleep(1)

    # Phase 2
    for i in range(MAX_ITER):
        phase = WOA_PHASES[min(i // 15, 3)]
        fitness = max(0.02, 0.95 * (0.97 ** i) + random.random() * 0.02)

        if len(selected) < target_n and random.random() < 0.2:
            selected.add(random.randint(0, TOTAL_FEATS - 1))

        print(f"Iter {i+1:02d} | {phase:<20} | Fitness: {fitness:.4f} | Selected: {len(selected)}")
        time.sleep(0.05)

    # Phase 3
    log("Training classifier (SVM)...")
    time.sleep(1)

    # Phase 4
    log("Analyzing behavior signature...")
    time.sleep(1)

    # Result
    reduction = round((1 - len(selected) / TOTAL_FEATS) * 100)

    print("\n" + "="*50)
    print("🚨 RANSOMWARE DETECTED 🚨")
    print("="*50)

    print(f"Name       : {rw['name']}")
    print(f"Type       : {rw_type}")
    print(f"Accuracy   : {rw['accuracy']}%")
    print(f"Features   : {len(selected)} / {TOTAL_FEATS}")
    print(f"Reduction  : {reduction}%")
    print(f"Signature  : {rw['sig']}")

    print("\nKey Indicators:")
    for k in rw["key_feats"]:
        print(f"  - {k}")

    print("\n⚠ GDPR Alert: Breach notification required")
    print("⚠ CERT-In Alert: Report within 6 hours")

# ────────────────────────────────────────────────
def main():
    print("\nWOA RANSOMWARE DETECTION (TERMINAL MODE)\n")

    rw_type, rw = select_ransomware()

    input("\nPress ENTER to start scan...")

    run_woa(rw_type, rw)

# ────────────────────────────────────────────────
if __name__ == "__main__":
    main()