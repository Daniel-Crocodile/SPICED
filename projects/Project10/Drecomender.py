import pandas as pd
import numpy as np
from sklearn.decomposition import NMF

def new_user(ratings, movies, n_rows):
    '''
    '''
    ratings = pd.read_csv(ratings, nrows=n_rows) 

    #make a dict with movieId and title
    movies = pd.read_csv(movies, index_col=0)
    movies.drop(columns='genres', inplace=True)

    df_rating_movies = pd.merge(ratings, movies, how='inner', on='movieId')
    df_rating_movies.drop(columns=['timestamp','movieId'], inplace=True)
    return df_rating_movies


def model_rec(df):
    '''
    '''
    R = df.pivot(index='userId',
            columns='title',
            values='rating'
    )

    R= R.fillna(2.5)
    nmf = NMF(n_components = 150, 
            max_iter=3_000, 
            l1_ratio= 0.7) 
    nmf.fit(R) 

    # item feature matrix
    Q = pd.DataFrame(nmf.components_, columns=R.columns)

    # user feature matrix
    P = pd.DataFrame(nmf.transform(R), index=R.index)

    # Matrixmultiplication of Q and P
    R_hat = pd.DataFrame(np.dot(P,Q), columns=R.columns, index=R.index)

    # evaluate error
    nmf.reconstruction_err_
    return R, P, Q, nmf


def user_rec(dict, model):
    '''
    '''
    R, P, Q, nmf = model

    ranking = []
    for i in list(range(0,5)):
        ranking.append(dict[sorted(dict.keys())[i]])

    titel = []
    for i in list(range(5,10)):
        titel.append(dict[sorted(dict.keys())[i]])

    dict_user = {titel[i]:ranking[i] for i in range(len(titel))}

    new_user = pd.DataFrame(dict_user, index=['new_user'], columns=R.columns)
    new_user = new_user.fillna(2.54)

    user_P = nmf.transform(new_user)

    user_R = pd.DataFrame(np.dot(user_P, Q), columns=R.columns, index=['new_user'])

    recommendations = user_R.drop(columns=titel)

    rec_user = list(recommendations.sort_values(axis=1, by='new_user', ascending=False))

    return rec_user[:5]
