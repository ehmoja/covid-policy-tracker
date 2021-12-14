import * as ReduxPromise from 'redux-promise';
import createSagaMiddleware from 'redux-saga';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import { createStore, applyMiddleware } from 'redux';
import rootReducer from './ducks/rootReducer';

const persistConfig = {
  key: 'root',
  storage,
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

export default function configureStore() {
  const sagaMiddleware = createSagaMiddleware();

  const store = createStore(
    persistedReducer,
    applyMiddleware(ReduxPromise, sagaMiddleware)
  );

  const persistor = persistStore(store);

  return { store, persistor, sagaMiddleware };
}
