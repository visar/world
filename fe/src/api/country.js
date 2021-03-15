import { useState } from 'react'
import Request from 'utils/Request'

const Country = () => {
  const [country, setCountry] = useState([])
  const [errorMessage, setErrorMessage] = useState([])
  const [isLoading, setLoading] = useState(true)

  const getCountryByCountryCode = async (countryCode) => {
    setLoading(true)
    try {
      const response = await Request.get(`/countries/${countryCode}`)
      setCountry(response.data)
      setLoading(false)
    } catch (error) {
      setErrorMessage([error.message])
      setLoading(false)
    }
  }

  return [getCountryByCountryCode, country, errorMessage, isLoading]
}

export default Country
