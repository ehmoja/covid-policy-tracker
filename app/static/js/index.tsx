// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import 'core-js/stable';

import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import { Router, Route, Switch } from 'react-router-dom';
import DocumentTitle from 'react-document-title';

import { BrowserHistory } from 'utils/navigationUtils';

import NotFoundPage from './pages/NotFoundPage';

import configureStore from './configureStore';
import rootSaga from './ducks/rootSaga';
import HomePage from 'pages/HomePage';

const { store, persistor, sagaMiddleware } = configureStore();

sagaMiddleware.run(rootSaga);

ReactDOM.render(
  <DocumentTitle title="Corona AI">
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <Router history={BrowserHistory}>
          <div id="main">
            {/* Page component */}
            <Switch>
              <Route exact path="/" component={HomePage} />
              <Route component={NotFoundPage} />
            </Switch>
          </div>
        </Router>
      </PersistGate>
    </Provider>
  </DocumentTitle>,
  document.getElementById('content') || document.createElement('div')
);
