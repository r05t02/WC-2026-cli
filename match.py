def main():
    import sys
    import datetime

    # READ DATA FROM LOCAL .JSON FILE
    import json
    with open('matches.json','r') as f:
        match_data = json.load(f)
        matches = match_data["matches"]
        print(type(matches))
        convert_to_indian_format(matches)
        
 
    # #OR PULL DATA DIRECTLY FROM URL
    # import requests
    # url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
    # match_data = requests.get(url).json()
    # matches = match_data["matches"]
    # convert_to_indian_format(matches)
    







# convert time, date to indian format
def convert_to_indian_format(match_list):

    num_of_matches = len(match_list)

    for items in range(num_of_matches):
            # DATE EXTRACTION AND FORMAT FIXING
            match_date = match_list[items]["date"]
            match_date = match_date.split("-")
            year = match_date[0]
            day = match_date[2]
            month = match_date[1]

            # CHANGING THE DATE FORMATS
            match_list[items]["date"] = f"{day}/{month}/{year}"
            fixed_date = match_list[items]["date"]


            #EXTRACT TIME
            match_time = match_list[items]["time"]
            exact_match_timings = match_date
            
            
          

            # UTC TO IST CONVERSION
            # IST = UTC + 5 HOURS 30 MINS

























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







