from add_order import AddOrder

try:
    with AddOrder() as bot:
        bot.land_first_page()
        bot.navigate_order_page()
        bot.fill_merchant_details()
        bot.fill_important_details()
        bot.fill_area_of_service_details()

except Exception as e:
    raise e