from rapidfuzz import process, fuzz
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "names.txt"

def load_names():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    return names

def get_matches(query, names, limit=10, scorer=fuzz.WRatio):
    results = process.extract(query, names, scorer=scorer, limit=limit)
    return results

def main():
    names = load_names()
    print(f"✅ Loaded {len(names)} names from dataset.")
    while True:
        query = input("\nEnter a name (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("👋 Exiting the program.")
            break
        results = get_matches(query, names, limit=10)
        best = results[0]
        print(f"\n🔹 Best Match: {best[0]} (Score: {best[1]:.2f})")
        print("\n🔸 Top 10 Similar Names:")
        for r in results:
            print(f"  {r[0]:25s}  Score: {r[1]:.2f}")
        output = {
            "query": query,
            "best_match": {"name": best[0], "score": best[1]},
            "matches": [{"name": r[0], "score": r[1]} for r in results]
        }
        print("\nJSON Output:")
        print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
