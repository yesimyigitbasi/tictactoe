import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

file_path = 'tic_tac_toe_dataset.csv'
data = pd.read_csv(file_path)

data[['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']] = pd.DataFrame(
    data['GameState'].apply(eval).to_list()
)
X = data.drop(columns=['GameState', 'BestMove'])
y = data['BestMove']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

accuracy

# using the trained model

def predict_best_move(game_state, model, starter, player_turn):
    input_data = game_state + [player_turn, starter]
    predicted_move = model.predict([input_data])[0]
    return predicted_move

example_game_state = [1, 2, 0, 0, 0, 0, 0, 1, 0] 
starter = 1 
player_turn = 2 

best_move = predict_best_move(example_game_state, model, starter, player_turn)
best_move
