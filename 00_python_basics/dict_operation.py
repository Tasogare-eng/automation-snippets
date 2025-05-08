scores = {"Alice": 90, "Bob": 75}
scores["Carol"] = 82
for name, score in scores.items():
    print(f"{name}: {score}")
print(scores.get("Alice"), scores.get("David", "Not found"))