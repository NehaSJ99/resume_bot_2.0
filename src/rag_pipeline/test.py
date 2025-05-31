from graph.builder import build_app

def test_query(question: str):
    print(f"\n Running adaptive RAG pipeline for question: {question}")
    app = build_app()

    result = app.invoke({"question": question})

    print("\n Final Answer:")
    print(result["generation"])
    return result

if __name__ == "__main__":
    test_query("Who is Neha Jagtap?")
