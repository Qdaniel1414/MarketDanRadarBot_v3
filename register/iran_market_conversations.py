from handlers.iran_market.formulas.gold18_conversation import (
    gold18_conversation,
)


def register_iran_market_conversations(app):
    print("🔥 REGISTER IRAN MARKET CONVERSATIONS")

    app.add_handler(gold18_conversation)

    print("✅ GOLD 18 CONVERSATION REGISTERED")