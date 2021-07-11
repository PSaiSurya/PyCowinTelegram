import requests
import datetime
import time
import dictdiffer
import urllib3
import fake_useragent


DIST_ID = 00 # Your District ID
num_days = 5 # No of days to check. 5 days is ideal within the API Query limit
age = 25 # Your Age
my_agent = fake_useragent.UserAgent()
old_response_json = {}
new_response_json = {}


def cur_time():
    current_time = "(" + (
            datetime.datetime.now().utcnow() +
            datetime.timedelta(hours=5.5)).strftime("%d/%m/%Y %H:%M:%S") + ")"
    return current_time

def countdown(t):
    while t:
        timer = f'{t} Seconds '
        print("Waking up in " + timer, end="\r")
        time.sleep(1)
        t -= 1


def get_dates():
    base = datetime.datetime.today().utcnow() + datetime.timedelta(hours=5.5)
    date_list = [base + datetime.timedelta(days=x) for x in range(num_days)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]
    return date_str


def telegram_bot_send_text(bot_message):
    bot_token = '' # Your Bot token. See Readme.md for more details
    channel_id = '' # Your Channel ID. See Readme.md for more details
                    # For example, if your ID is -1001234567890, Enter "1234567890"(without quotes)
    send_channel = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-100' + channel_id + '&parse_mode=HTML&text=' + bot_message
    response = requests.get(send_channel)
    if 400 <= response.status_code <= 499:
        print("Client Side Error encountered ", response.status_code)
    elif 500 <= response.status_code <= 599:
        print("Server Side Error encountered ", response.status_code)
    return response.json()


def get_header():
    try:
        my_agent = fake_useragent.UserAgent(use_cache_server=False)
        browser_header = {'User-Agent': my_agent.random}
    except fake_useragent.errors.FakeUserAgentError:
        browser_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    except fake_useragent.errors:
        browser_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    except:
        browser_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    return browser_header


def get_response(date_str, browser_header, json):
    for each_date in date_str:
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={DIST_ID}&date={each_date}"
        try:
            response = requests.get(url,
                                    headers=browser_header,
                                    timeout=(7, 12.5))
            if response.ok:
                resp_json = response.json()
                json[each_date] = resp_json
                response.close()
            elif response.status_code == 403:
                print("Request Forbidden by Server ", cur_time())
                response.close()
            else:
                print("Weird Response from Server ", cur_time())
                print(response.text)
                response.close()
        except TimeoutError:
            print("Timeout Error ", cur_time())
            break
        except requests.exceptions.ConnectionError as e:
            print("Connection Error ", cur_time())
            print(e)
            break
        except urllib3.exceptions.TimeoutError:
            print("Socket timeout error ", cur_time())
            break
        except urllib3.exceptions.RequestError:
            print("Urllib3 Requests error ", cur_time())
            break


def print_slots(resp_json, center_name, the_date):
    if resp_json["sessions"]:
        for center in resp_json["sessions"]:
            if center["name"] == center_name:
                if center["min_age_limit"] <= age:
                    if center["available_capacity"] > 0:
                        if center["available_capacity_dose1"] == 0:
                            result = f"""
    1) Name: <b><i>{center["name"]}</i></b>
    2) Area: <i>{center["block_name"]}</i>
    3) Address: <i>{center["address"]}</i>
    4) Availability date: <i>{the_date}</i>
    5) Price: <i>₹.{center["fee"]}/-</i>
    6) Total Available Capacity: <b>{center["available_capacity"]}</b>
        (Dose 1 - <b><i>{center["available_capacity_dose1"]}</i></b>; Dose 2 - <b><i>{center["available_capacity_dose2"]}</i></b>)
    <b>Dose 1</b> is not available
    7) Vaccine: <b><i>{center["vaccine"]}</i></b>

    Data Retrieved from CO-WIN Portal on {cur_time()}
    Access Co-WIN here : https://selfregistration.cowin.gov.in
        """
                        elif center["available_capacity_dose2"] == 0:
                            result = f"""
    1) Name: <b><i>{center["name"]}</i></b>
    2) Area: <i>{center["block_name"]}</i>
    3) Address: <i>{center["address"]}</i>
    4) Availability date: <i>{the_date}</i>
    5) Price: <i>₹.{center["fee"]}/-</i>
    6) Total Available Capacity: <b>{center["available_capacity"]}</b>
        (Dose 1 - <b><i>{center["available_capacity_dose1"]}</i></b>; Dose 2 - <b><i>{center["available_capacity_dose2"]}</i></b>)
    <b>Dose 2</b> is not available
    7) Vaccine: <b><i>{center["vaccine"]}</i></b>

    Data Retrieved from CO-WIN Portal on {cur_time()}
    Access Co-WIN here : https://selfregistration.cowin.gov.in
    """
                        else:
                            result = f"""
    1) Name: <b><i>{center["name"]}</i></b>
    2) Area: <i>{center["block_name"]}</i>
    3) Address: <i>{center["address"]}</i>
    4) Availability date: <i>{the_date}</i>
    5) Price: <i>₹.{center["fee"]}/-</i>
    6) Total Available Capacity: <b>{center["available_capacity"]}</b>
        (Dose 1 - <b><i>{center["available_capacity_dose1"]}</i></b>; Dose 2 - <b><i>{center["available_capacity_dose2"]}</i></b>)
    7) Vaccine: <b><i>{center["vaccine"]}</i></b>

    Data Retrieved from CO-WIN Portal on {cur_time()}
    Access Co-WIN here : https://selfregistration.cowin.gov.in
                                """
                        #print(result) # For more details, Head to FAQ-1 of Readme.md
                        telegram_bot_send_text(result) #FAQ-1
                        print("Message Sent to telegram channel ", cur_time()) #FAQ-1
    else:
        print(f"No available slots on {the_date}")

def check_for_update(resp1, resp2):
    old_capacity = {
        centre["name"]: centre["available_capacity"]
        for centre in resp1['sessions']
    }
    new_capacity = {
        centre["name"]: centre["available_capacity"]
        for centre in resp2['sessions']
    }
    incr_li = []
    diff_list = list(dictdiffer.diff(new_capacity, old_capacity))
    print(diff_list)
    for diff in diff_list:
        if diff[0] == 'change':
            new_slots = diff[2][0] - diff[2][1]
            if new_slots >= 3: # Notify only if 3 or more new slots are opened 
                incr_li.append(diff[1])
        elif diff[0] == 'add':
            incr_li.append(diff[1])
        elif diff[0][0] == 'add':
            incr_li.append(diff[0][2][0][0])
        elif diff[0] == 'remove' and diff[1] == "":
            for item in diff[2]:
                for hosp in item:
                    if type(hosp) == type("String"):
                        print(item[0])
                        incr_li.append(hosp)
    return incr_li

if __name__ == "__main__":
    Header = get_header()
    while True:
        dates = get_dates()
        get_response(dates, Header, old_response_json)
        print("Response 1 received. Waiting for Response 2", cur_time())
        print("Sleeping....")
        countdown(60)
        get_response(dates, Header, new_response_json)
        print("Response 2 received. Checking for new slots ", cur_time())
        for date in dates:
            try:
                increased_centers = check_for_update(old_response_json[date],
                                                     new_response_json[date])
                if len(increased_centers) == 0:
                    print(f"No new slots are available on {date} ", cur_time())
                else:
                    for each_centre in increased_centers:
                        print_slots(new_response_json[date], each_centre, date)
            except KeyError:
                print("Handling Key Error ", cur_time())
                continue
