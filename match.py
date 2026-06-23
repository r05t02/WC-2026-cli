from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import json
import sys
def main():

    # READ DATA FROM LOCAL .JSON FILE
    with open('matches.json','r') as f:
        match_data = json.load(f)
        matches = match_data["matches"]
        # print(matches)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        convert_to_indian_format(matches)
        for x in range(len(matches)):
            print(matches[x])
        
        
        

        
 
    # #OR PULL DATA DIRECTLY FROM URL
    # import requests
    # url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
    # match_data = requests.get(url).json()
    # matches = match_data["matches"]
    # convert_to_indian_format(matches)
    







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

            
             
            







if __name__ == "__main__":
    main()










# date = input("DATE: ")

# for x in range(len(matches)):
#     if date == matches[x]["date"]:
#         print(matches[x])
#         time = matches[x]["time"]
#         time = time.split(":")
#         kick_off_HOUR = time[0]
        




















##Implement option to find match using command line
# fixture = sys.argv[1]
# fixture = fixture.split(" vs ")
# print(fixture)


##Implement option to find matches of a particular team using command line







