import Request from 'utils/Request'
import { useState } from 'react'

const Regions = () => {
  const [regions, setRegions] = useState([])
  const [errorMessage, setErrorMessage] = useState([])
  const [isLoading, setLoading] = useState(true)

  const getRegionsByContinent = async (continent) => {
    setLoading(true)
    try {
      const response = await Request.get(`/regions?continent=${continent}`)
      setRegions(response.data)
      setLoading(false)
    } catch (error) {
      setErrorMessage([error.message])
      setLoading(false)
    }
  }

  return [getRegionsByContinent, regions, errorMessage, isLoading]
}

export default Regions
