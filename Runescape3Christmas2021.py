#A program to estimate the total amount of christmas wrapping paper I would earn through gameplay during the Runescape 3 Christmas Event 2021.

paper_per_hour = 354 #exact amount of christmas wrapping paper gathered in one hour of average gameplay
present_cost = 200 #amount of wrapping paper required to purchase one event present
days = 21 #the amount of days the event runs for
daily_playtime = 3 #average hours played per day

print("Welcome to SpamAtHomes' Runescape 3 Christmas event rewards estimation extravaganza! This program is designed to calculate and output the estimated rewards earned throughout the duration of the 2021 event.  ")

#estimated christmas wrapping paper earned per minute
def paper_per_minute(hourlyrate, seconds):
  return paper_per_hour / 60

minutely_rate = paper_per_minute(paper_per_hour, 60)
minutely_rate = float(minutely_rate)
print("Your estimated minutely paper earned is " + str(minutely_rate))

#estimated christmas wrapping paper earned per day
def paper_per_day(hourlyrate, playtime):
  return paper_per_hour * daily_playtime

daily_paper = paper_per_day(paper_per_hour, daily_playtime)
print("Your estimated daily paper earned from this event is " + str(daily_paper))

#estimated christmas wrapping paper earned in total
def event_total_paper(amount, playtime):
  return daily_paper * days

total_estimate = event_total_paper(daily_paper, days)
print("Your estimated total earned paper throughout the duration of this event is " + str(total_estimate))

#estimated christmas present rewards earned per hour
def presents_per_hour(hourly_paper, cost):
  return paper_per_hour / present_cost

hourly_presents = presents_per_hour(paper_per_hour, present_cost)
print("Your estimated hourly presents earned throughout the event is " + str(hourly_presents))

#estimated christmas present rewards earned per day
def presents_per_day(daily):
  return hourly_presents * daily_playtime

daily_presents = presents_per_day(daily_playtime)
print("Your estimated daily presents earned throughout the event is " + str(daily_presents))

#estimated christmas present rewards earned per week
def presents_per_week(weekly):
  return daily_presents * 7

weekly_presents = presents_per_week(daily_paper)
print("Your estimated weekly presents earned throughout the event is " + str(weekly_presents))

#estimated christmas present rewards earned in total
def event_presents_total(total_amount, days):
  return weekly_presents * days

total_earned = event_presents_total(weekly_presents, days)
print("Your estimated total amount of presents earned during the event is " + str(total_earned))


#rounded total number of presents earned
rounded_total = round(total_earned)
print("As you can't obtain a fraction of a present, the final estimated total of presents earned during Runescape 3's 2021 Christmas event is " + str(rounded_total))

#chance to earn green santa hat - will calculate when more data is released

#remaining paper at end of event after claiming all present rewards
leftover_paper = total_estimate % 200
print("As one event present costs " + str(present_cost) + " you would have " + str(leftover_paper) + " event paper remaining.")
