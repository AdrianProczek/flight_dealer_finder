import data_manager
import flight_search
import datetime as dt
import notification_manager

sheet_data = data_manager.DataManager()
search_flight = flight_search.FlightSearch()
sheet_data.get_destination_data()

origin_city_code = "LON"

for row in sheet_data.destination_data:
    if row["iataCode"] == "":
        row["iataCode"] = search_flight.search_iata_code(row["city"])
sheet_data.update_data()

tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
plus_6_months = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")

for row in sheet_data.destination_data:
    flight = search_flight.check_flights(origin_city_code, row["iataCode"], tomorrow, plus_6_months)

    if int(flight.price) < int(row["lowestPrice"]):
        notification_manager.NotificationManager.send_sms(message=
                                                          f"Low price alert! Only {flight.price} to fly from "
                                                          f"{flight.origin_city}-{flight.origin_airport} to "
                                                          f"{flight.destination_city}-{flight.destination_airport}, "
                                                          f"from {flight.out_date} to {flight.return_date}."
                                                          )

