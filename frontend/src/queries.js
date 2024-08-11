import gql from 'graphql-tag';


export const allCategories = gql`
query{ 
allCategories{
  categoryName,
  
}
}
`

export const allManufactuers = gql`

query{
  allManufactuers{
    manufName
    manufAgency
  }
}
`;

export const supportsCo = gql`
  query {
  allSupportcompany {
    companyName
    companyPhon1
  }
}
  `;


export const supportCoByName = gql`
  query($companyName: String!) {
  supportCompanyByName(companyName : $companyName){
  id
}
}
`;

  export const CompanyByName = gql`
  query($expertcompany: String!){
  companyExpertsByCompany(expertcompany : $expertcompany){
    expertFistName
    expertLastName
  	expertMobile
    expertcompany{
      companyName
      id
    }
    
  }
}
  `

export const AllExpertName = gql`
query{
  allCompanyexperts{
    expertFistName
    expertLastName
    expertMobile
    expertcompany {
      companyName
      companyPhon1
    }
  }
}
`


export const allBranches = gql`
  query 
      {
        allBranches{
            branchCode
            branchName
            branchDgree
            branchPersonNo
        } 
      }
  `;

export const USER_SIGNUP = gql`
mutation ($username: String!, $email: String!, $password: String!) {
  createUser(username: $username, email: $email, password: $password) {
    user {
      id
      username
    }
  }
}
`;

export const CURRENT_USER = gql`
  query ($username: String!) {
    currentUser(username: $username) {
      id
      username
      firstName
      lastName

      
        
    }
  }
`;