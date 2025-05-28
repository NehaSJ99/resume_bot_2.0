from graph.builder import build_app

def main():
    # Build the graph
    app = build_app()

    # Define input state
    input_state = {
        "question": "Who is Neha Jagtap?",
    }

    # Invoke the graph with the question
    output = app.invoke(input_state)

    # Print final generated answer
    print("\n Final Answer:\n")
    print(output["generation"])

if __name__ == "__main__":
    main()