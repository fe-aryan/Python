import requests

def get_country_info(country_code):
  url = "https://restcountries.eu/v2/alpha/" + country_code
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None

def get_state_info(country_code, state_code):
  country_info = get_country_info(country_code)
  if country_info is not None:
    for region in country_info["regions"]:
      if region["isoCode"] == state_code:
        return region
  return None

def get_district_info(country_code, state_code, district_name):
  state_info = get_state_info(country_code, state_code)
  if state_info is not None:
    for district in state_info["districts"]:
      if district["name"] == district_name:
        return district
  return None
