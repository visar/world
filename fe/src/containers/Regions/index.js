import React, { useEffect } from 'react'

import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import useRegions from 'api/regions'

import { useParams, useHistory } from 'react-router-dom'
import Alert from '@material-ui/lab/Alert'
import Divider from '@material-ui/core/Divider'
import ListSubheader from '@material-ui/core/ListSubheader'

const Regions = () => {
  const params = useParams()
  const history = useHistory()

  const [getRegionsByContinent, regions, errorMessage, isLoading] = useRegions()

  useEffect(() => {
    getRegionsByContinent(params.continent)
  }, [])

  const navigateTo = (region) => {
    history.push(`/${params.continent}/${region.name}`, { region })
  }

  if (isLoading) {
    return (<Alert severity="info">Loading...</Alert>)
  }

  return (
    (errorMessage.length)
      ? <Alert severity="error">{errorMessage}</Alert>
      : <List>
        <ListSubheader>Regions</ListSubheader>
        <Divider />
        {regions.data.map((region) =>
          <ListItem button onClick={() => navigateTo(region)}>
            <ListItemText primary={`${region.name}`} />
          </ListItem>
        )}
      </List>
  )
}

export default Regions
