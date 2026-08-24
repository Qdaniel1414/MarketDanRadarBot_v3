"""
موتور محاسبات طلا
تمام فرمول‌های طلا در این فایل قرار می‌گیرند.
"""


def calculate_gold18(
    weight: float,
    price_per_gram: float,
    ojrat_percent: float,
    profit_percent: float,
    tax_percent: float,
):
    """
    محاسبه قیمت طلای ۱۸ عیار

    ورودی‌ها:
        weight          وزن (گرم)
        price_per_gram  قیمت هر گرم طلای ۱۸
        ojrat_percent   اجرت
        profit_percent  سود
        tax_percent     مالیات

    خروجی:
        dict
    """

    base_price = weight * price_per_gram

    ojrat_amount = base_price * (ojrat_percent / 100)

    subtotal = base_price + ojrat_amount

    profit_amount = subtotal * (profit_percent / 100)

    taxable_amount = ojrat_amount + profit_amount

    tax_amount = taxable_amount * (tax_percent / 100)

    final_price = subtotal + profit_amount + tax_amount

    return {

        "base_price": round(base_price),

        "ojrat_amount": round(ojrat_amount),

        "profit_amount": round(profit_amount),

        "tax_amount": round(tax_amount),

        "final_price": round(final_price),

    }