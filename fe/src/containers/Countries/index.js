import React, { useEffect } from 'react'

import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import useCountries from 'api/countries'

import Alert from '@material-ui/lab/Alert'

import Divider from '@material-ui/core/Divider'
import ListSubheader from '@material-ui/core/ListSubheader'

import { useParams, useHistory } from 'react-router-dom'

const Countries = () => {
  const params = useParams()
  const history = useHistory()

  const [getCountriesByContinent, countries, errorMessage, isLoading] = useCountries()

  useEffect(() => {
    getCountriesByContinent(params.region)
  }, [])

  const navigateTo = (country) => {
    history.push(`/${country.continent}/${country.region}/${country.code}`, { country })
  }

  if (isLoading) {
    return (<Alert severity="info">Loading...</Alert>)
  }

  return (
    (errorMessage.length)
      ? <Alert severity="error">{errorMessage}</Alert>
      : <List>
        <ListSubheader>Countries</ListSubheader>
        <Divider />
        {countries.data.map((country) =>
          <ListItem button onClick={() => navigateTo(country)}>
            <ListItemText primary={`${country.name}`} />
          </ListItem>
        )}
      </List>
  )
}

export default Countries
