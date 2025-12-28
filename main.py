from graph import router_graph

while True:
    question = input("Enter your question: ")
    if question.lower() in ("stop", "стоп"):
        break
    ans = router_graph.invoke({"question": question})

print("end routing")