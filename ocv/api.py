import requests


def getUniPrice(setl, carType):
    url = "https://apiintegrity.universalna.com/osago"
    user = "Integrity"
    password = "1234$qwerty"
    data = "{\"personType\" : \"NATURAL\",\"vehicleType\" : \"" + carType + "\",    \"taxi\" : false," \
           "    \"privilegeType\" : \"NO\",    \"registrationPlace\" : \"" + setl + "\",    \"drivingSkills\" : " \
                                                                                    "\"more3\"} "

    r = requests.post(url=url, data=data, auth=(user, password,))
    m = r.json()
    return m['payment']
