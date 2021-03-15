import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Continents from 'containers/Continents'
import Countries from 'containers/Countries'
import Country from 'containers/Country'
import React from 'react'
import Regions from 'containers/Regions'

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
