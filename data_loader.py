import pickle

def load_events(path):
    with open (path, 'rb') as f:
        data = pickle.load(f)
    return data

