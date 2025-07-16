import React from 'react'

const De_com = (props) => {
    const { name,age,city,country } = props.myStudent
  return (
    <div>
        <h3>my name is {name} and my age is {age} </h3>
        <h3>my city is {city} {country}</h3>
      
    </div>
  )
}

export default De_com