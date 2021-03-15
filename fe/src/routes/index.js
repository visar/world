import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Continents from 'containers/Continents'
import Regions from 'containers/Regions'
import Countries from 'containers/Countries'
import Country from 'containers/Country'

const Routes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Continents} />
        <Route exact path="/:continent" component={Regions} />
        <Route exact path="/:continent/:region" component={Countries} />
        <Route exact path="/:continent/:region/:countryCode" component={Country} />
      </Switch>
    </BrowserRouter>
  )
}

export default Routes
