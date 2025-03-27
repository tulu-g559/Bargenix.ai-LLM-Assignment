Negotiation Chatbot Project Documentation🚀
=========================================

**Project Overview**

This project implements a negotiation chatbot for Bargenix.ai, a Kolkata-based company. The chatbot processes bargaining dialogues, responds with street-smart negotiation tactics using the Gemini API, and is deployed via a FastAPI endpoint. The focus is on data preprocessing, prompt engineering, and API deployment, tailored to an Indian context with rupees (₹).

- **Developed By**: [Arnab Ghosh](https://github.com/tulu-g559)
- **GitHub Repo**: [Bargenix.ai-LLM-Assignment](https://github.com/tulu-g559/Bargenix.ai-LLM-Assignment)

Project Structure
-----------------
```
negotiation_chatbot/
├── data/
│   └── raw_conversations.txt      # Raw negotiation dataset
├── nltk_task1.py                
├── negotiation_bot_task2.py             
├── api_task3.py                         
├── .env                           # API key storage
└── negotiation_data.json          # Processed data output
```
#
Task 1: Process & Structure Negotiation Data
--------------------------------------------

**File**: `nltk_task1.py`

**Purpose**: Converts raw text-based negotiation dialogues into structured JSON.

**Key Features**:

*   **Input**: data/raw\_conversations.txt (alternating User/Bot lines).
*   **Preprocessing**: Lowercasing, punctuation removal (except ₹), tokenization using NLTK.
*   **Output**: negotiation\_data.json with user\_message and bot\_response pairs.
    

**Sample Input**:

User: Hey, I like this jacket. How much is it?

Bot: It’s ₹80, boss! Top-quality stuff.

**Sample Output**:
```
[
{"user_message": "hey i like this jacket how much is it", "bot_response": "its ₹1100 boss top quality stuff"}
]
```
**Execution**: 
```
python nltk_task1.py
```
**Notes**:

*   Preserves ₹ for Indian rupees, aligning with the Kolkata context.
*   Handles incomplete pairs by skipping them.
    
#
Task 2: Implement LLM-Based Negotiation Bot
-------------------------------------------

**File**: `negotiation_bot_task2.py`

**Purpose**: Creates a chatbot that negotiates using the Gemini API (gemini-2.0-flash).

**Key Features**:

*   **LLM Integration**: Uses Google’s Gemini API with a custom system prompt.
*   **Prompt Engineering**: Defines a witty, tough Indian vendor persona; enforces ₹ usage.
*   **Logic**: Rejects low offers, suggests counteroffers, adds urgency, and maintains context via chat history.
    
*   **Dependencies**: 
```
google-generativeai 
python-dotenv 
```

**System Prompt**:
```
SYSTEM_PROMPT ="""        
You are a witty, street-smart vendor from Kolkata selling high-demand fashion items.
You never give big discounts right away—bargaining is a game, and you're the boss!
If a user offers too low, push back with supply-demand logic and some local sass.
Use Indian Rupees (₹), throw in terms like 'arre', 'dada', 'bhai', but conversation should be in proper english
Keep it short, sharp, and full of Kolkata market charm. 
Negotiate in Indian Rupees for now       
"""
```
**Sample Interaction**:
```
 bot = NegotiationBot()

    # Test interaction
    print(bot.generate_response("Hey, I like this jacket. How much is it?", base_price=1100))
    print(bot.generate_response("Can I get a discount?"))
    print(bot.generate_response("₹700?"))
    print(bot.generate_response("Give me in 700, or I will go"))
    print(bot.generate_response("Dont go for these tactics with me, I will get the same thing in any other shop"))
```
**Check video for more insights**
#
Task 3: Deploy FastAPI Chatbot API
----------------------------------

**File**: `api_task3.py`

**Purpose**: Deploys the negotiation bot as a RESTful API using FastAPI.

**Key Features**:

*   **Endpoint**: /bargain (POST)
*   **Input**: JSON with user\_offer and base\_price (e.g., `{"user_offer": 300, "base_price": 500}`).
*   **Output**: JSON with bot’s response (e.g., `{"response": "₹475, final offer—decide now!"}`).
*   **Dependencies**: 
```
fastapi
uvicorn
```    

**Sample API Call**:
```
curl -X POST "http://localhost:8000/bargain" -H "Content-Type: application/json" -d '{"user\_offer": 300, "base\_price": 500}'
```
**Sample Response**:
`{"response": "₹300? No chance, bhai! This is premium stuff. ₹475 if you grab it now—tick-tock!"}`

**Execution**:

```
python api_task3.py
````
#
Setup Instructions
------------------

1.  **Install Dependencies**:
`pip install google-generativeai fastapi uvicorn python-dotenv nltk`
    
2.  **Set API Key**:
    
    *   Create `.env` with GOOGLE\_API\_KEY=your-key-here.
        
3.  **Run Tasks**:
    
    *   **Task 1:** `python nltk_task1.py`
    *   **Task 2:** `python negotiation_bot_task2.py` (for testing)
    *   **Task 3:** `python api_task3.py`(then test with CURL/Postman)
        

Future Improvements
-------------------

*   Add price threshold logic (e.g., reject offers **< 60% of base price**).
*   Enhance preprocessing with stopwords removal.
*   Implement session management for multi-user API support.