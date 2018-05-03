from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd



def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)



scrabble_games = pd.read_csv("Turns.csv", dtype  = {"LineNum": "float64", "gameid":"float64" ,"turn_game":"float64", "player":"float64","pofloat64s":"float64","score":"float64","word_length":"float64","tiles_played":"float64","tiles_rack":"float64","turn_player":"float64","rack_value":"float64","rack_vowels":"float64","rack_consonants":"float64","rack_s":"float64","rack_blanks":"float64","tws":"float64","dws":"float64","tls":"float64","dls":"float64"})


clean_dataset(scrabble_games)

#scrabble_games.fillna(0) #remove the N/A categories.


scrabble_games['player'] = scrabble_games['player'].map({'Player1': 1, 'Player2': 0})


X = scrabble_games[0:]

X.drop("score", axis = 1) #drop the score from the x data. We're trying to predict score so it's not wanted as a parameter.
y = scrabble_games["score"]

X = X.as_matrix().astype(np.float)
y = y.as_matrix().astype(np.float)



X_train, Xtest, ytrain,  ytest = train_test_split(X, y) #split float64o training and test data.

scaler = StandardScaler() #normalize data. 
scaler.fit(X_train)

X_train = scaler.transform(X_train) #apply transformations to the data.
#Should avoid transforming the test data, as this might not be done with real values.


neural_net_regressor = MLPRegressor() #using default values. can change.
neural_net_regressor.fit(X_train, ytrain)

scrabble_games.shape()
print("Done with training. Can test")





