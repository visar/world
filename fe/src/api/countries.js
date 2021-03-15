import Request from 'utils/Request'
import { useState } from 'react'

const Countries = () => {
  const [countries, setCountries] = useState([])
  const [errorMessage, setErrorMessage] = useState([])
  const [isLoading, setLoading] = useState(true)

  const getCountriesByContinent = async (region) => {
    setLoading(true)
    try {
      const response = await Request.get(`/countries?region=${region}`)
      setCountries(response.data)
      setLoading(false)
    } catch (error) {
      setErrorMessage([error.message])
      setLoading(false)
    }
  }

  return [getCountriesByContinent, countries, errorMessage, isLoading]
}

export default Countries
