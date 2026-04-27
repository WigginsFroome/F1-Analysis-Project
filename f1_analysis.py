import fastf1
from matplotlib import pyplot as plt
from fastf1 import plotting

session = fastf1.get_session(2019, 12, 'R')
session.name
session.date

session.load()

event_name = session.event['EventName']
print('Event name: ', event_name)
print('Session name: ', session.name)
print('Session date: ', session.date)
print(session.results)
print(session.results.columns)

Q3_t10 = session.results.iloc[0:10].loc[:, ['Abbreviation', 'Q3']]
print("Top 10 Q3: ", Q3_t10)

df = session.results[['BroadcastName', 'Abbreviation', 'TeamName', 'CountryCode', 'GridPosition', 'Position', 'ClassifiedPosition', 'Time', 'Points', 'Status']]
print(df)

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

fig, ax = plt.subplots(figsize=(8, 5))

for driver in ('HAM', 'SAI', 'VER', 'ALB', 'RUS'):
    laps = session.laps.pick_drivers(driver).pick_quicklaps().reset_index()
    style = plotting.get_driver_style(identifier=driver,
                                      style=['color', 'linestyle'],
                                      session=session)
    ax.plot(laps['LapTime'], **style, label=driver)

# add axis labels and a legend
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
ax.legend()