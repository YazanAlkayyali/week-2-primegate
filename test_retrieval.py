from src.week_2_primegate.retrieval import search_chapter

results = search_chapter("what is a cookie-cutter business plan")
for r in results:
    print(r[:200])
    print("---")