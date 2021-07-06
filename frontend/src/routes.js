import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Login from  './pages/Login';
import Register from './pages/Register';
import Records from './pages/Records';
import PassReset from './pages/PassReset';
import Record from "./pages/Record";
import Validation from "./pages/Login/validation";

export default function Routes() {
    return(
        <BrowserRouter>
            <Switch>
                <Route path="/login" component={Login} />
                <Route path="/register" component={Register} />
                <Route path="/validation" component={Validation} />
                <Route path="/" exact component={Records} />
                <Route path="/:id" exact component={Record} />
                <Route path="/pass-reset" component={PassReset} />
            </Switch>
        </BrowserRouter>
    );
}