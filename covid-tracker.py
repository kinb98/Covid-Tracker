from covid import Covid
from datetime import datetime as dt

def covidUpdateWorldwide():
    total_active_cases = Covid().get_total_active_cases()
    total_confirmed_cases = Covid().get_total_confirmed_cases()
    total_recovered = Covid().get_total_recovered()
    total_deaths = Covid().get_total_deaths()

    print("Total Statistics")
    print(f"Total Active: {total_active_cases}")
    print(f"Total Confirmed: {total_confirmed_cases}")
    print(f"Total Recovered: {total_recovered}")
    print(f"Total Deaths: {total_deaths}")


def specific_country(country):
    country_info = Covid().get_status_by_country_name(country)
    total_active_cases = country_info['active']
    total_confirmed_cases = country_info['confirmed']
    total_recovered = country_info['recovered']
    total_deaths = country_info['deaths']
    updated_time_epoch = country_info['last_update']
    date_updated = dt.fromtimestamp(updated_time_epoch/1000)
    print(f"Total Statistics of {country}")
    print(f"Total Active: {total_active_cases}")
    print(f"Total Confirmed: {total_confirmed_cases}")
    print(f"Total Recovered: {total_recovered}")
    print(f"Total Deaths: {total_deaths}")
    print(f"Lst Updated at: {date_updated}")

choice = input("Do you want to get the updates of the world or any other country ?. Type W for world and any other character for any country")
if choice == 'W':
    covidUpdateWorldwide()
else:
    country = input("Enter the name of the country: ")
    try:
        specific_country(country)
    except:
        print("There is no country with this name.")