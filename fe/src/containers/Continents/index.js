import React, { useEffect } from 'react'

import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import useContinents from 'api/continents'
import Alert from '@material-ui/lab/Alert'
import Divider from '@material-ui/core/Divider'
import ListSubheader from '@material-ui/core/ListSubheader'

import { useHistory } from 'react-router-dom'

const Continents = () => {
  const history = useHistory()
  const [getContinents, continents, errorMessage, isLoading] = useContinents()

  useEffect(() => {
    getContinents()
  }, [])

  const navigateTo = (continent) => {
    history.push(`/${continent.name}`, { continent })
  }

  if (isLoading) {
    return (<Alert severity="info">Loading...</Alert>)
  }

  return (
    (errorMessage.length)
      ? <Alert severity="error">{errorMessage}</Alert>
      : <List>
        <ListSubheader>Continents</ListSubheader>
        <Divider />
        {continents.data.map((continent) =>
          <ListItem button onClick={() => navigateTo(continent)}>
            <ListItemText primary={`${continent.name}`} />
          </ListItem>
        )}
      </List>
  )
}

export default Continents
