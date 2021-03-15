import React, { useEffect } from 'react'
import { useHistory, useParams } from 'react-router-dom'
import Alert from '@material-ui/lab/Alert'
import CircularProgress from '@material-ui/core/CircularProgress'
import Divider from '@material-ui/core/Divider'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import ListSubheader from '@material-ui/core/ListSubheader'
import useRegions from 'api/regions'

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
    return <CircularProgress />
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
