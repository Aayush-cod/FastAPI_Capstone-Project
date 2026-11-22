import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cached_prediction, set_cached_prediction

model = joblib.load(settings.MODEL_PATH)


def predict_car_price(data : dict):
    cached_key = " ".join([str(val) for val in data.values()])

    cached_data = get_cached_prediction(cached_key)

    if cached_data:
        return cached_data

    input_frame = pd.DataFrame([data])
    prediction = model.predict(input_frame)[0]
    set_cached_prediction(cached_key , prediction)
    return prediction

