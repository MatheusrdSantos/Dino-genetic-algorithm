# Dino-genetic-algorithm
This python project is a demonstration of what a genetic algorithm technique can achieve when applied in a game. The current game is the famous dinosaur game launched by google chrome.

<img src="https://user-images.githubusercontent.com/42742621/69763661-a6b09b00-114c-11ea-9bc4-aabc040e652b.gif" width="600px">

# python modules
- keyboard
- Tkinter
- numpy
- pillow

# Project scopes

In this project, there are three scopes: 'train', 'game' and 'simulation'. Each one has a different purpose to see the project running.

## train

You can run training mode through the following code:

```
python3 main.py train
```

The training mode uses a pre-trained set o dinos. After executing the above command the training will continue using the best dino of the last training.

## simulation

You can run the simulation mode through the following code:

```
python3 main.py simulation
```
The simulation mode is better when you want to see the dinos learning through each generation. This mode doesn't use any previous result as a start point. So each stating dino has a random behavior that changes as new generations are generated.

## game

You can run game mode through the following code:

```
python3 main.py game
```

In this mode, you can compete against the best dino you have trained. The dino with the highest score wins.
