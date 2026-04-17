#----------------------------
# Feature Engineering
#----------------------------

# Season from month
def get_season(month):
    if month in [11, 12, 1, 2]:
        return "Cool"
    elif month in [3, 4, 5]:
        return "Hot"
    else:
        return "Rainy"

bangkok_df['season'] = bangkok_df['month'].apply(get_season)
bangkok_df['quarter'] = ((bangkok_df['month'] - 1) // 3) + 1

bangkok_df[['month', 'season', 'quarter']].sample(10)