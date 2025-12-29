from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import Literal
from router import chain


# State
class RouterState(TypedDict):
    question: str
    category: str

# Nodes
def choose_agent(state: RouterState) -> RouterState:
    state['category'] = chain.invoke({"question": state['question']})
    return state

def document_agent(state: RouterState) -> RouterState:
    print("The message has been forwarded to the document agent.")
    return state

def tests_agent(state: RouterState) -> RouterState:
    print("The message has been forwarded to the entrance tests agent.")
    return state

def courses_agent(state: RouterState) -> RouterState:
    print("The message has been forwarded to the courses agent.")
    return state

def internships_agent(state: RouterState) -> RouterState:
    print("The message has been forwarded to the internships agent.")
    return state

def admissions_officier(state: RouterState) -> RouterState:
    print("The message has been forwarded to the admissions officer.")
    return state

# Edge
def route_question(state: RouterState) \
    -> Literal["document", "tests", "courses", "internships", "human support"]:
    cat = state['category']
    if cat == 'document submission':
        return "document"
    elif cat == 'entrance examinations':
        return "tests"
    elif cat == 'curriculum and courses':
        return "courses"
    elif cat == 'internships':
        return "internships"
    elif cat == 'other':
        return "human support"
    else:
        print(cat)
        return "support"

# Graph
builder = StateGraph(RouterState)

builder.add_node("choose agent", choose_agent)
builder.add_node("document", document_agent)
builder.add_node("tests", tests_agent)
builder.add_node("courses", courses_agent)
builder.add_node("internships", internships_agent)
builder.add_node("human support", admissions_officier)

# Edges
builder.add_edge(START, "choose agent")
builder.add_conditional_edges("choose agent", route_question)
builder.add_edge("document", END)
builder.add_edge("tests", END)
builder.add_edge("courses", END)
builder.add_edge("internships", END)
builder.add_edge("human support", END)

router_graph = builder.compile()

# Visualisation (optional)
if __name__ == "__main__":
    graph_vis = router_graph.get_graph()
    with open("img/graph.jpg", "wb") as f:
        f.write(graph_vis.draw_mermaid_png())