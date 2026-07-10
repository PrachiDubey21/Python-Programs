# # Data comes in the form of ->
#  {
#     "success": True,
#     "data": {
#         "login": {
#             "username": "john123"
#         },
#         "location": {
#             "country": "India"
#         }
#     }
# }


# requests is a Python library used to send HTTP requests.

#pip install requests
import requests

API_URL = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

def fetch_random_user():

    response = requests.get(API_URL)

    # convert response into a Python dictionary
    response_data = response.json()

    # if API request was successful
    if response_data.get("success"):

        user = response_data.get("data")

        username = user["login"]["username"]
        country = user["location"]["country"]

        return username, country

    # else if API returns failure
    raise Exception("Unable to fetch user details.")


def main():

    try:
        username, country = fetch_random_user()

        print("\nRandom User Details")
        print("-" * 25)
        print(f"Username : {username}")
        print(f"Country  : {country}")
        print("-" * 25)
        print()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()