import gql from "graphql-tag";

export const USER_SIGNIN = gql`
  mutation ($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
      user {
        id
        username
        firstName
        lastName
        
      
      }
    }
  }
`;

export const UPDATE_Expert = gql`
mutation (
  $expertFistName: String! ,
  $expertLastName: String! ,
  $expertMobile: BigInt! ,
  $expertcompany: ID! ,

 ) {
  UpdateExpert(
    expertFistName: $expertFistName   ,
    expertLastName: $expertLastName ,
    expertMobile: $expertMobile ,
    expertcompany: $expertcompany,

  ){
    UpdateExpert{
      expertMobile
    }
    }
  }

`
export const Delete_Expert = gql`
mutation ($expertMobile: BigInt!) {
  DeleteExpert(expertMobile: $expertMobile ){
    delExpert{
      expertMobile
    }
    }
  }

`

export const NEW_CATEGORY = gql`
mutation($categoryName: String!){
  NewCategory( categoryName: $categoryName){
    NewCat{
    categoryName
  }
  }
}`

export const DELETE_CATEGORY = gql`
mutation($categoryName: String!){
  DeleteCategory( categoryName: $categoryName){
    delCat{
    categoryName
  }
  }
}`


export const New_Expert = gql`
mutation (
  $expertFistName: String! ,
  $expertLastName: String! ,
  $expertMobile: BigInt! ,
  $expertcompany: ID! ,

 ) {
  CreateNewExpert(
    expertFistName: $expertFistName   ,
    expertLastName: $expertLastName ,
    expertMobile: $expertMobile ,
    expertcompany: $expertcompany,

  ){
    newExpert{
      expertMobile
    }
    }
  }

`
export const New_Company = gql`
mutation ($companyName: String! ,
  $companyPhon1: BigInt! ,
  $companyPhon2: BigInt! ,
  $companyPhon3: BigInt! ,
  $companyPhoneMobile: BigInt! ,
  $companyRank: Int! ,
  $companyCEOName: String!
 ) {
  createNewCompany(
    companyName:  $companyName ,
    companyPhon1: $companyPhon1 ,
    companyPhon2: $companyPhon2 ,
    companyPhon3: $companyPhon3  ,
    companyPhoneMobile: $companyPhoneMobile ,
    companyRank: $companyRank,
    companyCEOName : $companyCEOName,
  ){
    newCompany{
      companyCEOName
      companyPhon1
    }
  }
}

`

export const UPDATE_BRANCH = gql`
mutation($branchCode: Int! , $branchName:  String! , $branchDgree: String! , $branchPersonNo: Int!) {
  UpdateBranch(branchCode: $branchCode , branchName: $branchName , branchDgree: $branchDgree , branchPersonNo: $branchPersonNo){
  	upBranch {
      branchCode
      branchName
      branchDgree
      branchPersonNo
    }
  }
}
`

export const NEW_BRANCH = gql`
mutation($branchCode: Int! , $branchName:  String! , $branchDgree: String! , $branchPersonNo: Int!) {
  CreateNewBranch(branchCode: $branchCode , branchName: $branchName , branchDgree: $branchDgree , branchPersonNo: $branchPersonNo){
  	newBranch {
      branchCode
      branchName
      branchDgree
      branchPersonNo
    }
  }
}
`

export const DELETE_BRANCH = gql`
mutation($branchCode: Int!){
  DeleteBranch(branchCode: $branchCode ){
    delBranch {
      branchCode
    }
  }
}
`

export const NEW_MANUFACTURE = gql`
mutation($manufName: String! , $manufAgency: String!){
  CreateNewManufacture(
    manufName: $manufName,
    manufAgency: $manufAgency
  ){
    newManufacture{
    manufName
    manufAgency
  }
  }
}
`

export const DELETE_Manufactuer = gql`
mutation($manufName: String!){
  DeleteManufacture(manufName: $manufName){
    delManuf{
    manufName
  }
  }
}`