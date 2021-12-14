// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import * as React from 'react';
import * as DocumentTitle from 'react-document-title';

// TODO: Use css-modules instead of 'import'
import './styles.scss';

const NotFoundPage: React.FC<any> = () => {
  return (
    <DocumentTitle title="404 Page Not Found - Inbot">
      <main className="page-row">
        <div className="page-column not-found-page">
          <h1>404 Page Not Found</h1>
        </div>
      </main>
    </DocumentTitle>
  );
};

export default NotFoundPage;
