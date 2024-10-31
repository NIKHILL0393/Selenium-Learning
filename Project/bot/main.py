from booking.booking import Booking

with Booking() as bot:
   bot.land_first_page()
   print('Exiting.')
   bot.select_place_to_go('New Delhi')
   bot.select_dates(check_in_dates='2024-10-28',check_out_date='2014-10-30')
   bot.select_adults(6)
   bot.click_search()