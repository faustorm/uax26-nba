import pandas as pd

df = pd.read_csv("games.csv")

seasondf = df[df['SEASON'] == 2019]
seasondf["DIFF"] = abs(seasondf["PTS_home"] - seasondf["PTS_away"])

print(seasondf[["HOME_TEAM_ID", "VISITOR_TEAM_ID","PTS_home","PTS_away","DIFF"]])
