import React from "react"
import { useStaticQuery, graphql } from "gatsby"
import Image from "gatsby-image"

const Image48 = () => {
  const data = useStaticQuery(graphql`
    {
      allFile(filter: { extension: { eq: "png" } }) {
        edges {
          node {
            publicURL
            name
          }
        }
      }
    }
    `)
    }
