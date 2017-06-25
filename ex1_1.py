import pandas as pd
import numpy as np

SCRAPPING_DONE = 1

dedis = pd.read_csv('files/dedis-1.csv', sep=',', names=['email_hashed', 'movie_hashed', 'date', 'stars'],
                    skipinitialspace=True)
imdb = pd.read_csv('files/imdb-1.csv', sep=',', names=['email', 'movie', 'date', 'stars'], skipinitialspace=True)

# print(dedis_DF)
# print(imdb.iloc[10])

if not SCRAPPING_DONE:
    for i in range(imdb.shape[0]):
        for j in range(dedis.shape[0]):
            # conditions = [((dedis['date'] == imdb.iloc[i]['date'] ) & (dedis['stars'] != imdb.iloc[i]['stars'])),
            # ((dedis['date'] != imdb.iloc[i]['date'] ) & (dedis['stars'] == imdb.iloc[i]['stars'])),
            # ((dedis['date'] == imdb.iloc[i]['date'] ) & (dedis['stars'] == imdb.iloc[i]['stars']))]
            if ((dedis.loc[j]['date'] == imdb.loc[i]['date']) and (dedis.loc[j]['stars'] == imdb.loc[i]['stars'])):
                # and (imdb.iloc[j]['email'] == 'mohammad.yaghini@epfl.ch')):
                print("[imdb[{0}], dedis[{1}]]Match Found!, email: {2}, hashed_email:{3}, movie: {4}, hashed_movie: {5}"
                      .format(i, j, imdb.loc[i]['email'], dedis.loc[j]['email_hashed'], imdb.loc[i]['movie'],
                              dedis.loc[j]['movie_hashed']))
                # choices = ['D_only', 'S_only', 'both']

                # print(dedis.sort_values(by='Match', ascending=False))
else:
    hash = 'ce9f6dd91f5b7c6648bc76d3282fceb79b1c349a353836cac2a8def0e00c8379'
    matched_movie_hashes = dedis[dedis['email_hashed'].str.contains(hash)]['movie_hashed'].values.tolist()

    for item in matched_movie_hashes:
        print(item)
    # print(dedis[dedis['email_hashed'].str.contains(hash)]['movie_hashed'])