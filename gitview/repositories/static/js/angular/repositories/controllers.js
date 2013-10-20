GitView.repositories.controller("RepositoryController",
["Repository", "$scope", "$http", "$log", "$routeParams",
 function(Repository, $scope, $http, $log, $routeParams)
 {
     $scope.repository = Repository.get($routeParams.ownerName, $routeParams.repositoryName);

     $scope.repositoryTemplate = "/static/views/repository/tree.html";
 }]);
