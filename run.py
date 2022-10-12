from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input("Where you do you want to go? ")) #'New York'
        bot.select_dates(check_in_date=input("What is the check-in date? "), #'2022-10-16'
                         check_out_date=input("What is the check-out date? ")) #'2022-10-23'
        bot.select_adults(int(input("How many people?"))) #1
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()
 
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from the command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '   PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise

