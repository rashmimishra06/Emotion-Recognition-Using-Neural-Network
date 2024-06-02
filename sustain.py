from django.core.cache import cache
import pickle

model_cache_key = 'vocab_cache'
# this key is used to `set` and `get` your trained model from the cache

model = cache.get(model_cache_key)

if model is None:
    # your model isn't in the cache
    # so `set` it
    # load the pickle file
    model = pickle.load(open('polls/emotion_classification-model.pkl', 'rb'))
    cache.set(model_cache_key, model, None)
