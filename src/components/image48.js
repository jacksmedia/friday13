import React from "react"
import { Link, graphql } from "gatsby"

import Bio from "../components/bio"
import Layout from "../components/layout"
import SEO from "../components/seo"
import Image from "gatsby-image"

const Image48 = ({ data }) => {
  const post = data.markdownRemark

  return (
    <div>
      <section
        dangerouslySetInnerHTML={{ __html: post.html }}
        itemProp="image48px"
        className="oaktag"
      />
    </div>
  )
}

export default Image48

export const pageQuery = graphql`
  query Image48(
    $id: String!
  )
  { 
    markdownRemark(id: { eq: $id }) {
      id
      frontmatter {
        title
        description
        featuredimage {
          childImageSharp {
            fixed(width: 48, height: 48, quality: 95) {
              ...GatsbyImageSharpFixed
            }
          }
        }
      }
    }
  }
`
