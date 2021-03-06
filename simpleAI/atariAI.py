#!/usr/bin/env python3
import gym
import keras
import numpy as np
from scipy.misc import toimage
from imageProcessing import *

def transform_reward(reward):
	return np.sign(reward)

def fit_batch(model, gamma, start_state, 
	actions, rewards, 
	next_states, is_terminal):

	next_Q_values = model.predict([next_state, np.ones(actions.shape)])
	next_Q_values[is_terminal] = 0
	Q_values = rewards + gamma * np.max(next_Q_values, axis=1)

	model.fit(
		[cur_states, actions], actions * Q_values[:, None],
		nb_epoch=1, batch_size=len(start_states), verbose=0
		)

def atari_model(n_actions):
	ATARI_SHAPE = (4, 105, 80)

	frames_input = keras.layers.Input(ATARI_SHAPE, name='frames')
	actions_input = keras.layers.Input((n_actions,), name='mask')
	
	normalized = keras.layers.Lambda(lambda x: x / 255.0)(frames_input)

	conv_1 = keras.layers.convolution.Convolution2D(
		16, 8, 8, subsample=(4, 4), activation='relu'
		)(normalized)

	conv_2 = keras.layers.convolutional.Convolution2D(
		32, 4, 4, subsample=(2, 2), activation='relu'
		)(conv_1)

	conv_flattened = keras.layers.core.Flatten()(conv_2)

	hidden = keras.layers.Dense(256, activation='relu')(conv_flattened)

	output = keras.layers.Dense(n_actions)(hidden)

	filtered_output = keras.layers.merge([output, actions_input], mode='mul')

	self.model = keras.models.Model(input=[frames_input, actions_input], output=filtered_output)
	optimizer = keras.optimizers.RMSprop(lr=0.00025, rho=0.95, epsilon=0.01)
	self.model.compile(optimizer, loss='mse')

env = gym.make('BreakoutDeterministic-v4')

frame = env.reset()

env.render()

is_done = False
while not is_done:
	frame, reward, is_done, _ = env.step(env.action_space.sample())
	
	frame = preprocess(frame)
	env.render()
