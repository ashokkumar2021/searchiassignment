var express = require('express');
var { graphqlHTTP } = require('express-graphql');
var { buildSchema } = require('graphql');
const data = require('./final.json');

var schema = buildSchema(`
  type Query {
     news(category : String!) : [News]
     newsall(authors : String!) : [News]
  }

  type News {
    category: String
    headline : String
    authors : String
    link : String
    short_description : String
    date : String
  }
`);
 

const getNews = function(args){
  var category = args.category;
  return data.filter(news => {
    return news.category == category;
  })
}



var root = {
  news : getNews,
 // newsall : getNewsall
};
 




var app = express();
app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true,
}));
app.listen(4000, () => console.log('Now browse to localhost:4000/graphql'));