1. Why ARIMA?

I chose ARIMA (AutoRegressive Integrated Moving Average) for this analysis primarily because it is a robust and versatile model for time series forecasting, particularly suited to non-seasonal data. Given that the data did not exhibit significant seasonal patterns, ARIMA emerged as a more suitable choice compared to seasonal models like SARIMA (Seasonal ARIMA).

ARIMA's strength lies in its ability to model a wide range of time series data with its components: autoregression (AR), differencing (I), and moving average (MA). This model effectively captures the underlying trends and patterns in data, even in the absence of clear seasonality.

Furthermore, ARIMA's flexibility to integrate differencing helps in stabilizing the mean of a time series by removing changes in the level of a time series, thus addressing potential non-stationarity. This is crucial for achieving accurate forecasts in cases where the data may exhibit trends or cycles but not seasonal effects.

While other machine learning models can be powerful for various predictive tasks, their complexity and requirement for large datasets may not offer additional benefits for this specific scenario. ARIMA's simplicity and focus on time-dependent structures make it a more direct and interpretable choice for forecasting healthcare claims data.

2. Are ARIMA models based on machine learning, or are they solely statistical in nature?

I would say ARIMA is a real-time machine learning method.

Most machine learning methods are not real-time in the sense that the model is trained/validated with a given set of data and then used to process out-of-sample data.  During the training process, the model parameters are adjusted for optimal performance and are kept constant while using the model.

ARIMA model parameters are updated in real-time as new data is fed into the model. ARIMA has more a bottom-up structure, so it is less like neural network. At the end of the day, they all just use observation data to estimate parameters.

