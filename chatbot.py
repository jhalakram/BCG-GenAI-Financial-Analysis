# --- Task 2: Rule-Based Financial Chatbot (Dictionary Approach) ---

def financial_chatbot(query):
    # We use a dictionary to map user queries directly to responses
    responses = {
        "what is microsoft's revenue?": 
            "Microsoft's Total Revenue was $211.9B in 2023, $245.1B in 2024, and $281.7B in 2025.",
            
        "what is tesla's net income?": 
            "Tesla's Net Income declined from $15.0B in 2023 to $7.1B in 2024, and further to $3.8B in 2025.",
            
        "what is apple's revenue?": 
            "Apple's Total Revenue was $383.3B in 2023, $391.0B in 2024, and $416.2B in 2025.",
            
        "compare revenue": 
            "In 2025, Apple led with $416.2B in revenue, followed by Microsoft at $281.7B, and Tesla at $94.8B.",
            
        "what is apple's debt ratio?": 
            "For 2025, Apple has the highest Debt-to-Asset ratio (0.79), compared to Microsoft (0.44) and Tesla (0.39)."
    }
    
    # .get() looks for the query in the dictionary. 
    # If it finds it, it returns the value. If not, it returns the fallback message.
    # .lower() ensures capitalization doesn't break the search.
    return responses.get(query.lower().strip(), "I'm not sure how to answer that. Can you try a different question?")

# --- Command Line Interface ---
if __name__ == "__main__":
    print("--------------------------------------------------")
    print("Welcome to the GFC Financial Chatbot!")
    print("Type 'quit' to exit.")
    print("--------------------------------------------------")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
            
        response = financial_chatbot(user_input)
        print(f"Chatbot: {response}")
