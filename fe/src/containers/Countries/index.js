import React, { useEffect } from 'react'
import { useHistory, useParams } from 'react-router-dom'
import Alert from '@material-ui/lab/Alert'
import CircularProgress from '@material-ui/core/CircularProgress'
import Divider from '@material-ui/core/Divider'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import ListSubheader from '@material-ui/core/ListSubheader'
import useCountries from 'api/countries'

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
    return <CircularProgress />
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
