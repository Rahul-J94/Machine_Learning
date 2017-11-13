import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.mpl_style', 'default')
figsize(15, 3)
# not working
# url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
# url = url_template.format(month=3, year=2012)


# weather_mar2012 = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True, encoding='latin1')

csv = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv",parse_dates=True)
csv[u"PERCENT MALE"].plot(figsize=(15, 5))
# print (csv.head(5))