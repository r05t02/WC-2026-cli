from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import json
import sys
import requests

def main():
    ## PULL DATA DIRECTLY FROM URL
    # url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
    # match_data = requests.get(url).json()
    # matches = match_data["matches"]
    
                         #     OR      #

    #READ DATA FROM LOCAL .JSON FILE
    with open('matches.json','r') as f:
        match_data = json.load(f)    
    matches = match_data["matches"]


    #Replaces UTC to IST in dates and time
    convert_to_indian_format(matches)
    
    #sorts the matches list, by the using sort_matches as key (which returns a dateime object)
    matches.sort(key=get_match_sort_key)

    query = get_query()
   
    user_query_type = query_type(query)

    

    #CONTROL FLOW LOGIC BASED ON INPUT
    if user_query_type == "FIXTURE":
        search_fixture(query, matches)
    if user_query_type == "DATE":
       search_by_date(query, matches)
    if user_query_type == "ROUND":
        search_by_round(query, matches)
    if user_query_type == "SINGLE TEAM":
        search_team_matches(query, matches)




#CONVERT TIME AND DATE FROM UTC ---> IST FORMAT
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

#SORTS THE "MATCH" DICTIONARY BASED ON 
# Match sort key is a datetime object
def get_match_sort_key(match):
     
    #  for match in matches:
    #     full_ist_date = match["date"]
    #     full_ist_time = match["time"].replace(" IST", "")
    #     return datetime.strptime(f"{full_ist_date} {full_ist_time}", "%d/%m/%Y %H:%M")
     
         
    full_ist_date = match["date"]
    full_ist_time = match["time"].replace(" IST", "")

    match_date_and_time = f"{full_ist_date} {full_ist_time}"

    dt_object = datetime.strptime(match_date_and_time, "%d/%m/%Y %H:%M")

    return dt_object

#HANDLES THE PRESENCE/ABSENCE OF DIFF TYPES OF USER INPUT
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

#CATEGORIZE USER INPUT (QUERY) INTO DIFFERENT KINDS
def query_type(query):
    query = query.strip()

    stages = ["Matchday", "Round of 16", "Round of 32", "Quarter-final", "Semi-final", "Final"]
    # available_rounds = set(match["round"])
    
    if "vs" in query:
        return "FIXTURE"
    
    if "/" in query:
        return "DATE"
    
    for stage in stages:
            if stage.lower() in query.lower():
                return "ROUND"
            
    return "SINGLE TEAM"
   



##MAIN IMPLEMENTAION OF THE SEARCHING
#SEARCHES BY FIXTUES
def search_fixture(query, matches):
    query = query.strip()

    team_A, team_B = query.split(" vs ")

    # print(f"    Searching for: '{team_A}' vs '{team_B}'\n") ----- > makes it look like its taking time to search the entered fixture by user

   

    for match in matches:
        # if (match['team1'] == team_A or match["team2"] == team_A) and (match["team1"] == team_B or match["team2"] == team_B):
        if (match['team1'].lower() == team_A.lower() or match["team2"].lower() == team_A.lower()) and (match["team1"].lower() == team_B.lower() or match["team2"].lower() == team_B.lower()):

            team_one = match['team1']
            team_two = match["team2"]

            date = match["date"]
            time = match["time"]
            
            #print(match,"\n")     #->PRINTS THE FULL MATCH DICTIONARY CONTAINING THE FIXTURE SEARCHED BY USER

            print(" ╔══════════════════════════════════════════════╗")
            print("   ⚽", team_one, " vs ", team_two)
            print("   🏆", match["round"], " | ", match["group"])
            print("   📅", date, " 🕐 ", time )
            print("   📍", match["ground"])

            if match.get("score"):
                print("   🟢 Ongoing or Finsished")
            else:
                print("   🔴 Upcoming match")
            
            print(" ╚══════════════════════════════════════════════╝")

#SEARCH BY MATCH DATE
def search_by_date(query, matches):
    date = query
    # convert_to_indian_format(matches)
    date = date.strip()
    

    print(f"\n   📅 Matches on {date}\n")

    for match in matches:
        if match["date"]  == date:
            # print(match,"\n")
            print("   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── ")
            fixture = f"{match['team1']} vs {match['team2']}"
            print(f"   🕐 {match['time']} | {fixture:<45} {match['group']:<10} {match['round']:<15} {match['ground']}")
    print("   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── ")
           
#SEARCH ALL THE MATCHES IN A PARTICULAR ROUND
def search_by_round(query, matches):
    round = query.strip()
    print("  🏆 ", round.title())

    for match in matches:

        if match['round'].lower() == round.lower() or round.lower() in match["round"].lower():
            # print(match,"\n")
            date = match["date"]
            time = match["time"]
            round = match["round"]
            team_one = match["team1"]
            team_two = match["team2"]
            

            fixture = f"{team_one} vs {team_two}"

            print(" ───────────────────────────────────────────────────────────────")
            print(f"  📅  {date:<12} 🕐 {time:<20} |  {fixture:<45} ")
    print(" ───────────────────────────────────────────────────────────────")
            
#SEARCHES ALL MATCHES OF A PARTICULAR TEAM
def search_team_matches(query, matches):
    team = query.strip()

    print(f"{'🏆':>3}", team.title(), "Fixtures")

    for match in matches:
        if not match.get("team1") and not match.get("team2"):
            continue
    
        if match['team1'].lower() == team.lower() or match['team2'].lower() == team.lower():
            # print(match,"\n")
            date = match["date"]
            time = match["time"]

            team_one = match["team1"]
            team_two = match["team2"]
            fixture = f"{team_one} vs {team_two}"

            round = match["round"]
            ground = match["ground"]

            print(" ──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            # print("  📅 ", date, "  🕐 ", time, " | ", f"{fixture:<20}", round, ground)
            print(f"  📅 {date:<12} 🕐 {time:<10} | {fixture:<45} {round:<12} {ground}")
    print(" ──────────────────────────────────────────────────────────────────────────────────────────────────────────────")



if __name__ == "__main__":
    main()


##TODO A DATA STRUCTURE OF FLAGS OF EACH COUNTRY, TO DISPLAY ALONGSIDE MATCH DATA


##TODO
# Potential future commands:

#python match.py Argentina vs France 11/11/1111 semi
# python matches.py today          ????        | ---> Both these would require time calcs ??
# python matches.py next           ????        |
# python matches.py "group a"   ---> def get_match_by_round(round, matches) | -----|
#---------------------------------------------------------------------------]      |
# TODO                                                                             |
# input = sys.argv[1]                                                              |   
#                                                                                  | 
# if "vs" in input:                       < ---------------------------------------|

# elif looks_like_date(input):
#     search date

# elif round_exists(input):
#     search round

