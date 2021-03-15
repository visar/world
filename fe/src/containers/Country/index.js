import React, { useEffect } from 'react'
import { useHistory, useParams } from 'react-router-dom'
import Alert from '@material-ui/lab/Alert'
import CircularProgress from '@material-ui/core/CircularProgress'
import ListSubheader from '@material-ui/core/ListSubheader'
import Paper from '@material-ui/core/Paper'
import Table from '@material-ui/core/Table'
import TableBody from '@material-ui/core/TableBody'
import TableCell from '@material-ui/core/TableCell'
import TableContainer from '@material-ui/core/TableContainer'
import TableHead from '@material-ui/core/TableHead'
import TableRow from '@material-ui/core/TableRow'
import useCountry from 'api/country'

const Country = () => {
  const params = useParams()
  const history = useHistory()

  const [getCountryByCountryCode, country, errorMessage, isLoading] = useCountry()

  useEffect(() => {
    getCountryByCountryCode(params.countryCode)
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
      : <TableContainer component={Paper}>
        <Table aria-label="simple table">
          <TableBody>
            <ListSubheader>General information
                            <TableRow>
                <TableCell component="th" scope="row">Code</TableCell>
                <TableCell align="right">{country.code}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Name</TableCell>
                <TableCell align="right">{country.name}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Continent</TableCell>
                <TableCell align="right">{country.continent}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Region</TableCell>
                <TableCell align="right">{country.region}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Surface area</TableCell>
                <TableCell align="right">{country.surfacearea}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Independence year</TableCell>
                <TableCell align="right">{country.indepyear}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Population</TableCell>
                <TableCell align="right">{country.population}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Surface area</TableCell>
                <TableCell align="right">{country.surfacearea}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Life expectancy</TableCell>
                <TableCell align="right">{country.lifeexpectancy}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">GNP</TableCell>
                <TableCell align="right">{country.gnp}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Old GNP</TableCell>
                <TableCell align="right">{country.gnpold}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Local name</TableCell>
                <TableCell align="right">{country.localname}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Governmant form</TableCell>
                <TableCell align="right">{country.governmentform}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Head of state</TableCell>
                <TableCell align="right">{country.headofstate}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Other code</TableCell>
                <TableCell align="right">{country.code2}</TableCell>
              </TableRow>
            </ListSubheader>
            <ListSubheader>Capital
                            <TableRow>
                <TableCell component="th" scope="row">Name</TableCell>
                <TableCell align="right">{country.capital.name}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">District</TableCell>
                <TableCell align="right">{country.capital.district}</TableCell>
              </TableRow>
              <TableRow>
                <TableCell component="th" scope="row">Population</TableCell>
                <TableCell align="right">{country.capital.population}</TableCell>
              </TableRow>
            </ListSubheader>
            <ListSubheader>Cities
                                <Table>
                <TableRow>
                  <TableHead>
                    <TableCell component="th" scope="row">Name</TableCell>
                    <TableCell component="th" scope="row">District</TableCell>
                    <TableCell component="th" scope="row" align="right">Population</TableCell>
                  </TableHead>
                </TableRow>
                <TableRow>
                  {
                    country.cities.map((city) =>
                      <TableRow>
                        <TableCell align="left">{city.name}</TableCell>
                        <TableCell align="left">{city.district}</TableCell>
                        <TableCell align="right">{city.population}</TableCell>
                      </TableRow>
                    )
                  }
                </TableRow>
              </Table>
            </ListSubheader>
            <ListSubheader>Languages
                                <Table>
                <TableRow>
                  <TableHead>
                    <TableCell component="th" scope="row">Language</TableCell>
                    <TableCell component="th" scope="row" align="right">Percentage</TableCell>
                    <TableCell component="th" scope="row">Is official?</TableCell>
                  </TableHead>
                </TableRow>
                <TableRow>
                  {
                    country.languages.map((language) =>
                      <TableRow>
                        <TableCell align="left">{language.language}</TableCell>
                        <TableCell align="right">{language.percentage}</TableCell>
                        <TableCell align="left">{language.isofficial ? 'Official' : ''}</TableCell>
                      </TableRow>
                    )
                  }
                </TableRow>
              </Table>
            </ListSubheader>
          </TableBody>
        </Table>
      </TableContainer>
  )
}

export default Country
