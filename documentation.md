# GFC Financial Chatbot Technical Documentation

## 1. Rule-Based Architecture
The current prototype runs on a straightforward Python dictionary that maps specific user questions directly to their answers. We chose a dictionary setup to keep response times instant and logic simple. To prevent the chatbot from crashing when users ask unexpected questions, we implemented Python's `.get()` method. If a user query fails to match our dictionary keys, the system catches the exception and returns a helpful fallback error message instead of failing.

## 2. Data Storage & Retrieval Strategy
Right now, the chatbot answers are written directly into the code using the final insights from our earlier analysis phase. While this works perfectly for a quick prototype, it is not scalable. For the next development phase, we plan to connect this chatbot script to our structured `financial_data.csv` file using the Pandas library. This update will let the code scan and filter dataframes dynamically to calculate financial metrics on the fly whenever a user asks a question.

## 3. Financial Communication Design
Instead of just printing raw numbers that are hard to interpret, the chatbot translates data into short, meaningful summaries. For instance, when a user asks about Tesla, the bot explains the downstream impact—pointing out that dropping net income squeezed the final profit margins. Later updates will include an interactive loop that suggests related follow-up questions to help users navigate the financial data smoothly.

## 4. Current Limitations
*   **Exact Input Matching**: The code relies on simple string matching (lowercased). If a user makes a spelling mistake or structures their sentence differently, the script will miss the key and trigger the fallback response.
*   **Static Data Pool**: All financial numbers are fixed inside the code. The application cannot fetch real-time financial changes or pull data from live external APIs.
*   **No Language Processing (NLP)**: The script scans for keyword patterns but cannot understand user intent, context shifts, or the emotional tone behind a message.
