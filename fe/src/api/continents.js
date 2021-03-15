import { useState } from 'react'
import Request from 'utils/Request'

const Continents = () => {
  const [continents, setContinents] = useState([])
  const [errorMessage, setErrorMessage] = useState([])
  const [isLoading, setLoading] = useState(true)

  const getContinents = async () => {
    setLoading(true)
    try {
      const response = await Request.get('/continents')
      setContinents(response.data)
      setLoading(false)
    } catch (error) {
      setErrorMessage([error.message])
      setLoading(false)
    }
  }

  return [getContinents, continents, errorMessage, isLoading]
}

export default Continents
