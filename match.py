from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import json
import sys
import requests

def main():
    ## PULL DATA DIRECTLY FROM URL
    url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
    match_data = requests.get(url).json()
    matches = match_data["matches"]
    
    

    # READ DATA FROM LOCAL .JSON FILE
    # with open('matches.json','r') as f:
    #     match_data = json.load(f)
       
        
    # matches = match_data["matches"]

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    
    #Replaces UTC to IST in dates and time
    convert_to_indian_format(matches)
    

    #sorts the matches list, by the using sort_matches as key (which returns a dateime object)
    matches.sort(key=sort_matches)
    




    query = get_query()

    user_query_type = query_type(query)

    

    

    if user_query_type == "FIXTURE":
        search_fixture(query, matches)
    if user_query_type == "DATE":
       search_match_by_date(query, matches)
    # if user_query_type == "ROUND":
        #search_by_round(query):
    # if user_query_type == "SINGLE TEAM":
    #      #search_Team_matches(query)


    
 




    # try:
    #     fixture = sys.argv[1]
    #     team_a, team_b =fixture.split(" vs ")
    # except:
    #     team = input("Which team? ")

    # for match in matches:
    #     if team == match["team1"] or team == match["team2"]:
    #          print("Target found")
    #          print(match)
   
    # sorted_by_DateTime = sorted(matches, key=sort_matches)
    # print(sorted_by_DateTime)
    




# convert time, date to indian format
def convert_to_indian_format(match_list):

    num_of_matches = len(match_list)
    ist = ZoneInfo("Asia/Kolkata")

    for items in range(num_of_matches):
            # DATE EXTRACTION AND FORMAT FIXING
            match_date = match_list[items]["date"]
            match_time = match_list[items]["time"]

            #SPLIT THE MAIN PARTS REQUIRED FOR: UTC -> IST CONVERSION
            time, utc = match_time.split(" ")
            utc = utc.replace("UTC","")                 #Fixing UTC for datetime object conversion
            utc = int(utc)                              #Fixing UTC for datetime object conversion              
            match_datetime_str = match_date + " " + time

            original_data_timezone = timezone(timedelta(hours=utc))   #Fixing UTC for datetime object conversion
            match_dt_obj = datetime.strptime(match_datetime_str,"%Y-%m-%d %H:%M")    #converting Match date, time along with fixed UTC

            match_dt_obj = match_dt_obj.replace(tzinfo=original_data_timezone)
            # match_dt_obj is a datetime object with timezone as UTC


            #CONVERT TO IST
            
            match_dt_obj = match_dt_obj.astimezone(ist)
            
           
            #REPLACE THE DATE AND TIME (in Indian format) FROM THE ORIGINAL 'MATCHES' LIST
            #ORIGINAL 'MATCHES' LIST WILL GET MODIFIED
            ist_time = match_list[items]["date"] = match_dt_obj.strftime("%d/%m/%Y")
            ist_date = match_list[items]["time"] = match_dt_obj.strftime("%H:%M IST")

    # return ist_time, ist_date



def sort_matches(match):
     
    #  for match in matches:
    #     full_ist_date = match["date"]
    #     full_ist_time = match["time"].replace(" IST", "")
    #     return datetime.strptime(f"{full_ist_date} {full_ist_time}", "%d/%m/%Y %H:%M")
     
         
    full_ist_date = match["date"]
    full_ist_time = match["time"].replace(" IST", "")

    match_date_and_time = f"{full_ist_date} {full_ist_time}"

    dt_object = datetime.strptime(match_date_and_time, "%d/%m/%Y %H:%M")

    return dt_object



def get_query():
    if len(sys.argv) == 1:   #ONLY sys.argv[0] is there which is always name of the file
        user_inp = input("What do you want to look for? [Team, Fixture, Matches On A Date]  ")
        return user_inp
    else:
        user_inp = ""
        for x in range(len(sys.argv)):
            if x == 0:
                continue
            user_inp += sys.argv[x] + " "
        return user_inp

        
def query_type(query):
    query = query.strip()

    stages = ["Matchday", "Round of 16", "Round of 32", "Quarter-final", "Semi-final", "Final"]
    
    if "vs" in query:
        return "FIXTURE"
    
    if "/" in query:
        return "DATE"
    
    for stage in stages:
            if stage.lower() in query.lower():
                return "ROUND"
            
    return "SINGLE TEAM"
    
    
    
def search_fixture(query, matches):
    query = query.strip()

    team_A, team_B = query.split(" vs ")

    print(f"Searching for: '{team_A}' vs '{team_B}'")

   

    for match in matches:
        if (match['team1'] == team_A or match["team2"] == team_A) and (match["team1"] == team_B or match["team2"] == team_B):
            print(match)
            if match.get("score"):
                print("Match started (LIVE or FINISHED)")
            else:
                print("Upcoming match")


def search_match_by_date(query, matches):
    date = query
    # convert_to_indian_format(matches)
    date = date.strip()

    for match in matches:
        if match["date"]  == date:
            print(match,"\n")



    
        
          

     
                    
if __name__ == "__main__":
    main()






# TODO
# input = sys.argv[1]

# if "vs" in input:
#     search teams

# elif looks_like_date(input):
#     search date

# elif round_exists(input):
#     search round





#TODO - CLI IMPLEMENTATION 
##Implement option to find matches of a particular team using command line


#TODO
# Desired usage:

# python matches.py "Argentina"

# python matches.py "Argentina vs France"

# python matches.py "26/06/2026"

# python matches.py "round of 16"

# python matches.py "semi-final"





# Potential future commands:

#python match.py Argentina vs France 11/11/1111 semi

# python matches.py argentina

# python matches.py france

# python matches.py today          ????

# python matches.py next           ????

# python matches.py "group a"








