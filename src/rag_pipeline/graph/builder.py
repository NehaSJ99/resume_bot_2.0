from langgraph.graph import END, StateGraph, START
from graph.schema import GraphState
from graph.nodes import (
    retrieve,
    generate,
    grade_documents,
    transform_query,
    web_search
)
from graph.routes import (
    route_question,
    decide_to_generate,
    grade_generation_v_documents_and_question
)


def build_app():
    workflow = StateGraph(GraphState)

    # Define the nodes
    workflow.add_node("web_search", web_search)  # web search
    workflow.add_node("retrieve", retrieve)  # retrieve
    workflow.add_node("grade_documents", grade_documents)  # grade documents
    workflow.add_node("generate", generate)  # generate
    workflow.add_node("transform_query", transform_query)  # transform_query

    # Build graph
    workflow.add_conditional_edges(
        START,
        route_question,
        {
            "web_search": "web_search",
            "vectorstore": "retrieve",
        },
    )
    workflow.add_edge("web_search", "generate")
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_conditional_edges(
        "grade_documents",
        decide_to_generate,
        {
            "transform_query": "transform_query",
            "generate": "generate",
        },
    )
    workflow.add_edge("transform_query", "retrieve")
    workflow.add_conditional_edges(
        "generate",
        grade_generation_v_documents_and_question,
        {
            "not supported": "generate",
            "useful": END,
            "not useful": "transform_query",
        },
    )
    return workflow.compile()