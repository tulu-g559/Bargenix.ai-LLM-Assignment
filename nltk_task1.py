import json
import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt') 

def preprocess_text(text):
    """Basic NLP preprocessing: lowercase, remove punctuation except ₹, tokenize."""
    text = text.lower()
    text = re.sub(r'[^\w\s₹]', '', text)  # Keep ₹ for prices
    text = ' '.join(word_tokenize(text))  # Tokenize and rejoin
    return text.strip()

def parse_conversations(file_path):
    """Parse raw text into structured JSON."""
    with open(file_path, 'r', encoding='utf-8') as file:  # Added encoding
        lines = file.readlines()

    conversations = []
    for i in range(0, len(lines), 2):
        user_line = lines[i].strip()
        bot_line = lines[i + 1].strip() if i + 1 < len(lines) else None
        
        if bot_line is None:  # Skip incomplete pairs
            break
        
        user_message = preprocess_text(user_line.replace("User: ", ""))
        bot_response = preprocess_text(bot_line.replace("Bot: ", ""))
        
        conversations.append({
            "user_message": user_message,
            "bot_response": bot_response
        })
    return conversations

def save_to_json(data, output_path):
    """Save structured data to JSON."""
    with open(output_path, 'w', encoding='utf-8') as json_file:  # Added encoding
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    raw_file = "data/raw_conversations.txt"
    output_file = "negotiation_data.json"
    structured_data = parse_conversations(raw_file)
    save_to_json(structured_data, output_file)
    print(f"Data processed and saved to {output_file}")