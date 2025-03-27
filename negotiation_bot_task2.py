import os
from dotenv import load_dotenv
import google.generativeai as genai

# Loading key
load_dotenv() 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

SYSTEM_PROMPT = """
You are a witty, street-smart vendor from Kolkata selling high-demand fashion items.
You never give big discounts right away—bargaining is a game, and you're the boss!
If a user offers too low, push back with supply-demand logic and some local sass.
Use Indian Rupees (₹), throw in terms like 'arre', 'dada', 'bhai', but conversation should be in proper english
Keep it short, sharp, and full of Kolkata market charm. 
Negotiate in Indian Rupees for now
"""

# SYSTEM_PROMPT = """
# You are a tough street-smart negotiator selling high-demand fashion items. 
#         Never give big discounts immediately. If a buyer offers too low, explain supply-demand. 
#         Always counteroffer with a slight discount to make them feel they're winning. 
#         Create urgency in your replies (e.g., 'only if you buy now').
# """

# SYSTEM_PROMPT = """You are a tough, street-smart negotiator running a high-end fashion store in India, where bargaining is an art.
# You know the value of your products and never give big discounts right away. If a buyer offers too low, counter firmly, explaining quality, demand, and exclusivity.
# Use witty desi-style persuasion—mention limited stock, festive rush, and how others are eyeing the same item.
# Always counteroffer with a slight discount to make them feel like they are getting a deal, but keep margins intact.
# Use urgency tactics like 'Bhaiya, this is the last piece!', 'Offer valid only till you decide!', or 'Even my supplier won’t give this rate!'
# """

class NegotiationBot:
    def __init__(self):
        # Initialize chat with an empty history
        self.chat = model.start_chat(history=[])
        self.base_price = None
        self.last_offer = None
        # Manual history to track conversation
        self.history = []

    def generate_response(self, user_message, base_price=None):
        """Generate a negotiation response based on user input."""
        if base_price:
            self.base_price = base_price
        
        # Extract offer from user message if present
        offer = self._extract_offer(user_message)
        if offer is not None:
            self.last_offer = offer

        # Build the full prompt with system instruction and context
        full_prompt = f"{SYSTEM_PROMPT}\nBase price: ₹{self.base_price}\nUser: {user_message}\nBot:"

        # Send message to Gemini (no history passed directly, using prompt)
        response = self.chat.send_message(full_prompt).text.strip()

        # Update manual history
        self.history.append({"role": "user", "parts": [user_message]})
        self.history.append({"role": "assistant", "parts": [response]})

        return response

    def _extract_offer(self, message):
        """Extract numeric offer from user message."""
        import re
        match = re.search(r'[₹]?(\d+)', message)
        return int(match.group(1)) if match else None

if __name__ == "__main__":
    bot = NegotiationBot()

    # Test interaction
    print(bot.generate_response("Hey, I like this jacket. How much is it?", base_price=1100))
    print()
    print(bot.generate_response("Can I get a discount?"))
    print()
    print(bot.generate_response("₹700?"))
    print()
    print(bot.generate_response("Give me in 700, or I will go"))
    print()
    print(bot.generate_response("Dont go for these tactics with me, I will get the same thing in any other shop"))