import pandas as pd
import numpy as np

import keras
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM, RNN, SimpleRNNCell, SimpleRNN
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io


keras.models.load_model(
    "dj.h5",
    custom_objects=None,
    compile=False
)

class SampleResult(keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs={}):

        start_index = random.randint(0, len(text) - maxlen - 1)

        for diversity in [0.2, 0.5, 1.0, 1.2]:
            generated = ''
            sentence = "Keef"
            generated += sentence
            print()
            print('----- Generating with diversity',
                  diversity, 'seed: "' + sentence + '"')
            sys.stdout.write(generated)

            for i in range(100):
                x = np.zeros((1, maxlen, len(chars)))
                for t, char in enumerate(sentence):
                    x[0, t, char_indices[char]] = 1.

                preds = self.model.predict(x, verbose=0)[0]
                next_index = sample(preds, diversity)
                next_char = indices_char[next_index]

                generated += next_char
                sentence = sentence[1:] + next_char

                sys.stdout.write(next_char)
                sys.stdout.flush()
        print('\n\n')
sample_callback = SampleResult()

history = model.fit(X, y, 
                        epochs=10, 
                        batch_size=512,
                        verbose=2,
                       callbacks=[sample_callback])

