from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from negotiation_bot_task2 import NegotiationBot

app = FastAPI(title="Negotiation Chatbot API")
 
# Input model
class UserOffer(BaseModel):
    user_offer: int
    base_price: int

# Start the bot
bot = NegotiationBot()

# route for bargeain
@app.post("/bargain")
async def bargain(offer: UserOffer):
    """Handle user offer and return bot response."""
    try:
        user_message = f"Can I get it for ${offer.user_offer}?"
        response = bot.generate_response(user_message, base_price=offer.base_price)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)