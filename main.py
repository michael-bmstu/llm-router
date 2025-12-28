from graph import router_graph

while True:
    question = input("Enter your question: ")
    if question.lower() == "stop":
        break
    ans = router_graph.invoke({"question": question})
    
print("end routing")